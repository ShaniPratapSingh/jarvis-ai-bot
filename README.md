# jarvis-ai-bot
# 🎤 Jarvis AI Voice Auction Agent

A smart Python-based voice assistant that enables users to interact with a real-time auction system using natural speech. Designed for **OmniDimension Code Clash (Problem 2)**, this voice agent reads auction details aloud, accepts voice-based bids, and updates a live backend — all through simple conversations.

---

## 🧩 Problem Statement

> **Voice Agent for Real-Time Auction Participation and Bidding**

This project solves the challenge of fast-moving online auctions, where users often miss bids due to delay. The agent connects to a simulated auction backend, fetches real-time bidding data, speaks it to the user, and accepts voice bids that are validated and recorded — all via audio interface.

---

## ✨ Features

- 🎙️ Voice command support (SpeechRecognition + pyttsx3)
- 🔄 Real-time auction system with bid tracking
- 🧠 Validates and submits voice bids (only accepts higher)
- 🗂️ Logs all bidding activity (with optional dashboard)
- 🌐 Flask backend with RESTful API for auction data

---

## 📦 Tech Stack

| Area         | Tools / Libraries                      |
|--------------|----------------------------------------|
| Voice Agent  | Python, `speechrecognition`, `pyttsx3` |
| API Backend  | Flask                                  |
| Integration  | `requests` for voice-to-backend calls  |
| Optional UI  | HTML, JavaScript (Dashboard)           |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ShaniPratapSingh/jarvis-ai-bot.git
cd jarvis-ai-bot
2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
# .venv\Scripts\activate.bat   # Windows
3. Install all dependencies
pip install -r requirements.txt
4. Start the auction backend
cd auction_backend
python app.py
5. Run the Jarvis voice assistant
cd ..
python jarvis.py
✅ Speak naturally! The bot will respond to auction-related voice commands.

All voice commands are routed through logic and validated before submitting to the backend.

📁 Project Structure
graphql
jarvis-ai-bot/
├── jarvis.py                  # Voice assistant logic
├── auction_backend/
│   ├── app.py                 # Flask API for auction
│   └── data.json              # Auction products & bid history
├── requirements.txt
├── .gitignore
└── README.md
🔮 Future Improvements
Integrate OmniDimension’s webhook or call API

Natural language understanding using LLMs

Deployed web-based auction dashboard

Support for multi-user conversations

🙌 Built For
OmniDimension Code Clash (June 17–28, 2025)
🔗 Code Clash Info

Author: Shani Pratap Singh
