# ⌨️ Python Keylogger with Email Reporting ✉️

A simple yet powerful keylogger that logs keystrokes and sends them to your email inbox at regular intervals using Python. Built with `pynput`, `smtplib`, and `threading`, it’s a great project to learn how to capture input, use environment variables, and work with SMTP protocols.

> ⚠️ **Educational Purpose Only** – This tool is meant for ethical use, learning, and personal systems you have permission to monitor. Misuse may violate laws.

---

## 🚀 Features

- ⌨️ Captures alphanumeric and special keystrokes  
- 📩 Sends keystroke logs to your email  
- 🔁 Auto-reports at defined intervals (default: 60 seconds)  
- 🔧 Uses `.env` for secure credential management  
- 🧠 Clean and well-documented code with emoji-enhanced comments  
- ⛔ Stops on pressing `ESC`  

---

## 📂 Project Structure

```bash
keylogger/
│
├── keylogger.py       # 🔑 Core keylogger script (run this)
├── main.py            # 🚀 Entry point (runs keylogger)
├── .env               # 🔒 Store your email and credentials here
├── README.md          # 📘 You're reading it
└── LICENSE            # 📜 MIT License
