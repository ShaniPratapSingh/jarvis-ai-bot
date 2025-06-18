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
