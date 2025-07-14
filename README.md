# Ai_assistant
# 🎙️ Python Voice Assistant

This is a simple voice-controlled AI assistant built using Python. It can perform tasks like speaking the current time, searching Wikipedia, playing YouTube videos, and opening websites — all using your voice!

---

## 🚀 Features

- 🧠 Voice recognition via microphone
- 🗣️ Text-to-speech responses
- 🔍 Wikipedia summary search
- 🎵 Play songs on YouTube
- 🌐 Open popular websites (YouTube, Google, Facebook, ChatGPT)
- ⏱️ Tell the current time
- 🛑 Exit on command

---

## 🛠️ Technologies Used

- [Python 3.x](https://www.python.org/)
- [`pyttsx3`](https://pypi.org/project/pyttsx3/) – Text-to-Speech (offline)
- [`speech_recognition`](https://pypi.org/project/SpeechRecognition/) – Recognizes your voice
- [`wikipedia`](https://pypi.org/project/wikipedia/) – Fetches summaries
- [`webbrowser`](https://docs.python.org/3/library/webbrowser.html) – Opens sites
- [`pywhatkit`](https://pypi.org/project/pywhatkit/) – YouTube playback and more

---

## 📦 Installation

### Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/voice-assistant.git
cd voice-assistant
Step 2: Install dependencies
bash
Copy
Edit
pip install pyttsx3 SpeechRecognition wikipedia pywhatkit
You may also need to install pyaudio:

bash
Copy
Edit
pip install pyaudio
If you face installation issues with PyAudio, refer to platform-specific guides.

▶️ How to Run
Simply run the Python file:

bash
Copy
Edit
python assistant.py
You'll be greeted and then can start speaking commands like:

"What is Python on Wikipedia"

"Play Shape of You"

"Open Google"

"Tell me the time"

"Stop" or "Exit" to end the session

💡 Example Commands
Say this...	Assistant will...
"Play Believer"	Play the song on YouTube
"Wikipedia Albert Einstein"	Speak a summary from Wikipedia
"Open YouTube"	Launch YouTube in your browser
"What time is it"	Tell the current system time
"Stop" or "Exit"	End the assistant

🧠 Future Improvements
Add weather forecast

Use GPT-based AI for better natural conversation

Save query logs or history

Add GUI interface

📄 License
This project is open-source and available under the MIT License.

🙌 Acknowledgements
Thanks to the Python open-source community.

Voice services powered by Google Speech API.
