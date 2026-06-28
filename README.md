# 🤖 Rule-Based Chatbot with Google Search Automation

A Python-based conversational chatbot that uses rule-based pattern matching to understand user intent and responds with text-to-speech output. When a search query is detected, it automatically launches Google Chrome and performs a live Google search using Selenium.

---

## ✨ Features

- **Pattern-Based Intent Detection** — Recognises greetings, goodbyes, negative/personal questions, and search queries using keyword matching
- **Text-to-Speech Responses** — Every bot reply is spoken aloud using `pyttsx3`
- **Google Search Automation** — Detects search intent and opens a real Google Chrome browser to perform the search via Selenium
- **Randomised Responses** — Greetings and goodbye replies are randomised for a more natural feel
- **Input Sanitisation** — Strips punctuation from user input before processing
- **Clean Exit** — Type `_EXIT_` to gracefully quit the chatbot

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.x |
| Text-to-Speech | `pyttsx3` |
| Browser Automation | `selenium` + ChromeDriver |
| Browser | Google Chrome |

---

## 📁 Project Structure

```
RULEBASED-CHATBOT/
├── app.py                # Main chatbot logic
├── Dependency.txt        # Installation instructions
├── Doc.pdf               # Project documentation
└── chromedriver_win32/   # ChromeDriver for Windows
```

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install pyttsx3
pip install selenium
```

### 2. Download ChromeDriver

Download the ChromeDriver that matches your installed Chrome version:
```
https://sites.google.com/chromium.org/driver/downloads
```
Place the `chromedriver.exe` inside the `chromedriver_win32/` folder (already included for Windows).

### 3. Run the Chatbot

```bash
python app.py
```

---

## 💬 How It Works

The chatbot processes user input through a pipeline:

```
User Input → Remove Punctuation → Split into Words → Pattern Matching → Response Selection → Speak + Print
```

### Intent Categories

| Intent | Trigger Keywords | Action |
|---|---|---|
| Greeting | hello, hi, hey, howdy, hola... | Random greeting response |
| Goodbye | bye, farewell, adieu, later... | Random farewell response |
| Search | search, find, what, look, explore... | Opens Google Chrome & searches |
| Negative | love, name, age, gender, hate... | Deflects with bot disclaimer |
| Exit | `_EXIT_` | Gracefully closes the chatbot |

### Example Conversation

```
YOU: Hello!
BOT: Hey!         ← spoken aloud

YOU: Search Python tutorials
BOT: Opening your Chrome Browser!   ← opens Chrome with Google search

YOU: _EXIT_
BOT: VISIT AGAIN!
```

---

## ⚙️ Configuration

You can tweak speech settings in `app.py`:

```python
engine.setProperty('rate', 130)   # Speed of speech (words per minute)
engine.setProperty('volume', 1)   # Volume (0.0 to 1.0)
```

---

## 📋 Requirements

- Python 3.x
- Google Chrome (installed on your system)
- ChromeDriver matching your Chrome version
- Windows OS (ChromeDriver included for `win32`)

---

## 📄 License

This project is open source and free to use for educational purposes.
