# ⌨️ Python Keylogger with Email Reporting ✉️

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6+-blue?logo=python" />
  <img src="https://img.shields.io/badge/License-MIT-green?logo=opensourceinitiative" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey?logo=windows" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?logo=github" />
</p>

<p align="center">
  <img src="https://media3.giphy.com/media/o6TTJ6ak4A97a/giphy.gif" width="400" alt="Hacker Python Coding">
</p>



<p align="center">
  <img src="https://i.imgur.com/k5jYKVI.png" width="600" alt="Keylogger Screenshot Example">
</p>



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
```

---

## 🛠️ Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/Anonymoussxb/keylogger.git
   cd keylogger
   ```

2. **Install Dependencies**
   You need Python 3.6+ and the following modules:

   ```bash
   pip install pynput python-dotenv
   ```

3. **Configure Environment Variables**
   Create a `.env` file in the same directory with the following:

   ```env
   FROM_EMAIL=your_email@gmail.com
   TO_EMAIL=receiver_email@gmail.com
   APP_PASS=your_app_password
   ```

   > 💡 Use [Google App Passwords](https://support.google.com/accounts/answer/185833) if you're using Gmail.

4. **Run the Keylogger**

   ```bash
   python keylogger.py
   ```

---

## ⚙️ How It Works

* The script starts listening for keystrokes using `pynput`.
* Keystrokes are stored in a buffer (`self.log`).
* Every 60 seconds, the log is sent to your email using SMTP.
* You can press `ESC` to stop the logger at any time.

---

## ✏️ Customization

* 🔁 To change the time interval, edit this line in `keylogger.py`:

  ```python
  self.time_count = 60  # Change to any number of seconds
  ```

* 📧 To send emails to a different address or from a different account, just update the `.env` file.

---

## ⚠️ Legal Disclaimer

This project is for **educational purposes only**. Running it on machines you do not own or have explicit permission to monitor is **illegal**. Use responsibly.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 💬 Connect

Feel free to contribute or raise issues.  
Made with ☕ by [Anonymoussxb](https://github.com/Anonymoussxb)
