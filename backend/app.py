from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import traceback

load_dotenv()

app = Flask(__name__)
# Enable CORS for all routes so the frontend can easily communicate with it
CORS(app)

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if api_key and api_key != "YOUR_GEMINI_API_KEY_HERE":
    genai.configure(api_key=api_key)

generation_config = {
  "temperature": 0.2,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 1024,
  "response_mime_type": "application/json",
}

system_instruction = """
You are an expert pair-programmer and code analyst. The user will provide a code snippet. 
Ignore any conversational filler. Return your analysis strictly as a JSON object with three keys: 
1. "explanation": a concise 1-2 sentence plain English summary of what the code does. 
2. "complexity": the time and space complexity of the algorithm.
3. "issues": any obvious bugs, security issues, or 'None' if it looks clean.
Do not include markdown formatting or backticks outside of the JSON structure.
"""

@app.route('/api/analyze', methods=['POST'])
def analyze():
    if not api_key or api_key == "YOUR_GEMINI_API_KEY_HERE":
        return jsonify({"error": "Gemini API Key missing! Please add it to backend/.env file and restart the server."}), 500

    data = request.json
    code_snippet = data.get("code")

    if not code_snippet:
        return jsonify({"error": "No code provided"}), 400

    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-pro",
            generation_config=generation_config,
            system_instruction=system_instruction
        )
        
        chat_session = model.start_chat()
        response = chat_session.send_message(code_snippet)
        
        # Parse output safely in case the model decides to wrap it in markdown block.
        response_text = response.text.strip()
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
            
        result = json.loads(response_text)
        return jsonify(result)
        
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
