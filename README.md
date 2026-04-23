# Devlens • AI Code Analyzer

Devlens is a powerful, AI-driven prototype designed to help developers instantly understand complex code snippets. Using the Gemini API, it provides a plain-English explanation, complexity analysis, and identifies potential bugs or security risks.

## ✨ Features
- **Glassmorphism UI:** A stunning, modern sky-blue interface.
- **Instant Analysis:** Powered by Google's Gemini 1.5 Pro.
- **Free Tech Stack:** Built using HTML/JS, Python Flask, and the free Gemini API tier.

## 🚀 Getting Started

### 1. Requirements
- Python 3.8+
- Gemini API Key ([Get it here](https://aistudio.google.com/))

### 2. Setup
1. Clone the repo.
2. Create a `backend/.env` file and add: `GEMINI_API_KEY=your_key_here`
3. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
4. Run the server:
   ```bash
   python app.py
   ```
5. Open `frontend/index.html` in your browser.

## 🛠 Built With
- **Frontend:** Vanilla HTML/CSS/JS (Glassmorphism design)
- **Backend:** Python Flask
- **AI Engine:** Google Gemini API
