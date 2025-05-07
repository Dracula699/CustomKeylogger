# CustomKeylogger
A basic yet effective Python keylogger that records keyboard input in real-time and saves it to a file. Useful for educational, ethical security testing, or personal productivity tracking. Records key events like letters, space, backspace, and enter — with duration-based logging control.

🎯 Features ------>

✅ Captures key presses in real-time

✍️ Logs text, spaces, newlines, and backspaces

🕒 Automatically stops after user-defined duration

💾 Saves logs to random.txt for later review

# Keyboard Typing Logger (Python)

This is a simple Python script that records everything you type for a specific amount of time and saves it to a text file called `random.txt`.

---

## What It Can Do

- Detects your key presses as you type.
- Handles basic keys like:
  - Letters
  - Spacebar
  - Backspace (removes the last character)
  - Enter (starts a new line)
- Automatically saves everything to a file.
- You decide how long it should keep recording.

---

## How to Run the Script

### 1. Download or Clone the Project

If you have Git installed, open your terminal and run:

```bash
git clone https://github.com/Dracula699/CustomKeylogger.git
cd KEYLOGGER
py keylogger.py

📁 Project Structure

📁 KEYLOGGER
├── keylogger.py
├── requirements.txt
└── random.txt

📦 Requirements
Install with:
pip install -r requirements.txt
