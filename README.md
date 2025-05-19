# PRODIGY_CS_04
# 🕵️ KeyLogger with Clipboard Monitoring

A Python-based keylogger that captures keyboard input and clipboard paste events (e.g., Ctrl+V or Cmd+V). The script logs every keystroke and clipboard data into a file with a timestamp, useful for educational and forensic purposes.

---

## ⚠️ Disclaimer

> 🚨 **For Educational Use Only**  
This tool is intended **strictly for ethical and educational purposes** (e.g., penetration testing on systems you own or have explicit permission to analyze). Unauthorized use may violate privacy laws and is illegal in many jurisdictions.

---

## 📌 Features

- 🧠 Logs all keystrokes with accurate timestamps
- 📋 Detects and logs clipboard paste actions
- ⌨️ Distinguishes between regular characters and special keys (Enter, Shift, etc.)
- 🗂 Outputs to a log file: `key_log.txt`

---

## 🛠️ Requirements

- Python 3.x
- `pynput`
- `pyperclip`

Install dependencies:

```bash
pip install pynput pyperclip
```

## 🚀 Usage
🔹 Run the keylogger
```bash
python keylogger.py
```
🔹 Log Output Example (key_log.txt)
```bash
[2025-05-19 11:22:15] Key: h
[2025-05-19 11:22:15] Key: e
[2025-05-19 11:22:15] Key: l
[2025-05-19 11:22:15] Key: l
[2025-05-19 11:22:15] Key: o
[2025-05-19 11:22:18] Special Key: [enter]
[2025-05-19 11:22:21] Clipboard Paste: secretpassword123
Logs are saved in the same directory as key_log.txt.
```
## 📂 Project Structure
```
├── keylogger.py
├── key_log.txt
└── README.md
```
## 🔐 Security & Ethical Use
✅ Use only on machines where you have explicit authorization.

❌ Never deploy or use on someone else’s computer or network without consent.

🧠 Designed for red team testing, ethical hacking education, and cybersecurity research.

## 📄 License
This project is released under the GNU GENERAL PUBLIC LICENSE Version 3.

