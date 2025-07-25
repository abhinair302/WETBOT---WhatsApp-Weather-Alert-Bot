# 🌧️ WETBOT - WhatsApp Weather Alert Bot

WETBOT is an automated weather alert bot that notifies you via **WhatsApp** if there's a high chance of **rain in the next 12 hours**.  
It uses **OpenWeatherMap** for weather forecasts and **Twilio**'s WhatsApp API to send alerts directly to your phone.

Designed for convenience, WETBOT ensures you're always prepared — even when the skies aren't!

---

## ✅ Features

- 🌦️ **Weather Forecast Check** using OpenWeatherMap (next 12 hours)
- 📲 **Instant WhatsApp Alert** if rain is predicted
- 🤖 Friendly AI tone in alerts (designed by Abhijeet Nair)
- 🔐 Uses `.env` file for secure API key and token handling
- 💡 Beginner-friendly Python code structure

---

## 💻 Requirements

Before you run this project, make sure you have:

### 🧰 Installed Software
- **Python 3.10 or higher**
- **pip (Python package manager)**
- **Twilio Account**

### 📦 Python Packages
Install required packages using:

```bash
pip install requests twilio python-dotenv
```


### 🔐 Environment Setup (.env File)
Create a file named .env (no file extension) in the same folder as your .py file.

Paste this inside it:
```
OWM_API_KEY=your_openweathermap_api_key
TWILIO_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
```

⚠️ Never share this file or push it to GitHub. It contains your private API credentials.


### 📲 Twilio WhatsApp Sandbox Setup
Go to: Twilio WhatsApp Sandbox

Follow the instructions to join the sandbox (send the given code via WhatsApp to +14155238886)

Use your full WhatsApp number in the code like:

YOUR_WHATSAPP_NO = "+91xxxxxxxxx"  # Replace with your number
💡 The sandbox only works with numbers that have joined it manually.


## 📸 Demo

Here’s what the WhatsApp alert looks like when rain is predicted:

![WETBOT WhatsApp Message](wetbot-demo.png)

Thank you for visiting and checking out WETBOT!
This is just the beginning — the project will continue to improve with time.
Stay dry, stay safe! ☂️💬

—
Created by Abhijeet Nair
