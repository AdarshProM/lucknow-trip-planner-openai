# 🏛️ Planning a Trip to Lucknow with OpenAI API

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📌 Project Overview

An AI-powered travel guide for **Lucknow, Uttar Pradesh** built using the **OpenAI GPT-4o-mini API**. This project demonstrates multi-turn conversation capabilities where the AI maintains context across multiple tourist questions about Lucknow landmarks.

## 🎯 What This Project Does

- Uses **OpenAI GPT-4o-mini** model as an intelligent travel guide
- Maintains **multi-turn conversation history** (AI remembers previous context)
- Answers tourist questions about Lucknow landmarks, distances, and attractions
- Demonstrates **prompt engineering** with system, user, and assistant roles
- Shows **API integration** with proper environment variable handling

## 🏙️ Sample Questions Answered

1. Distance from Hazratganj to Bada Imambara
2. Location of Hotel Taj Mahal in Lucknow
3. Must-see artworks at Lucknow State Museum

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python 3.8+ | Core programming language |
| OpenAI API (GPT-4o-mini) | AI language model |
| Multi-turn Conversations | Context-aware responses |
| Environment Variables | Secure API key management |

## 📁 Project Structure

lucknow-trip-planner-openai/
│
├── lucknow_trip_planner.py # Main application code
├── requirements.txt # Python dependencies
├── .env.example # Environment variable template
├── .gitignore # Git ignore rules
└── README.md # Project documentation

## ⚙️ How to Run This Project

### Step 1: Clone the Repository

git clone https://github.com/AdarshProM/lucknow-trip-planner-openai.git
cd lucknow-trip-planner-openai

Step 2: Install Dependencies

pip install -r requirements.txt

Step 3: Set Up API Key
# Copy the example file
cp .env.example .env

# Add your OpenAI API key to .env file
OPENAI_API_KEY=your_actual_api_key_here

Step 4: Run the Application
python lucknow_trip_planner.py

📊 Sample Output
text
============================================================
🏛️  AI Travel Guide: Planning a Trip to Lucknow
============================================================

📍 Question: How far away is the Hazratganj from the Bada Imambara?
----------------------------------------
🤖 AI Guide: Hazratganj is approximately 2 miles from Bada Imambara by road.

📍 Question: Where is the Hotel Taj Mahal?
----------------------------------------
🤖 AI Guide: Hotel Taj Mahal is located in the heart of Lucknow near...

============================================================
✅ Trip planning complete! Enjoy Lucknow!
============================================================
🔑 Key Concepts Demonstrated
OpenAI Chat Completions API - Making API calls with proper authentication

Multi-turn Conversations - Maintaining conversation history for context

Prompt Engineering - System, user, and assistant role configuration

Environment Variables - Secure handling of API credentials

Python Best Practices - Clean, documented, production-ready code

🚀 Future Enhancements
 Add more Lucknow landmarks and tourist spots

 Integrate Google Maps API for real-time distances

 Build a web interface using Flask/Streamlit

 Add speech-to-text for voice-based queries

 Deploy on cloud (AWS Lambda / Azure Functions / GCP Cloud Functions)

👨‍💻 Author
Adarsh Singh

LinkedIn: linkedin.com/in/narayanadarsh

Email: adarsh.narayan.official@outlook.com

Location: Lucknow, Uttar Pradesh, India

📜 License
This project is open source and available under the MIT License.

Built as part of cloud engineering portfolio to demonstrate AI/ML API integration skills
