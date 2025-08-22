# 🛡️ BlockApps

**BlockApps** is a powerful Python script that blocks **apps and websites** based on a customizable schedule.  
It works on **Windows** and **MacOS**, and is designed to be **very hard to bypass** — making it an effective tool for staying focused.

🔒 Built to help people stay productive during studies and work, especially after being disappointed by the limitations (and paywalls) of existing solutions.

---

## 🚀 Features

- 🖥️ Cross-platform support: **Windows** & **Linux**
- 🕐 Schedule-based blocking system (set hours/days)
- 🌐 Website blocking (via hosts file manipulation)
- 📦 App blocking (based on process name)
- 💪 Designed to be **resilient against tampering**
- 🧠 Lightweight and no GUI — focus on simplicity and control

---

## 💡 Why I Made This

I created **BlockApps** because most existing focus tools are either:

- Behind a paywall 💸  
- Easy to bypass 🫠  

This tool helped me **focus intensely** during study and work sessions, and I hope it can help others too.

---

## 🛠️ Requirements

- Python 3.7+
- Administrator/root privileges (required for blocking functionality)

---

## ⚙️ How It Works

For websites: Edits the system hosts file to redirect specified URLs to 127.0.0.1
For apps: Continuously checks for running processes and kills any that are on the blocklist
Uses a user-defined schedule (examples in presets.py)

---

## 🧪 Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/BlockApps.git
cd BlockApps
```

2. Edit presets.py to customize you schedule

3. Run the script with administrator privileges

### 👀 Recommended

Use pyarmor to crypt the python files and make it impossible to edit the presets.py or any file

---

## ⭐️ Star the repo if you find it helpful!
