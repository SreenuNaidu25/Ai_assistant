import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', engine.getProperty('voices')[0].id)  # [0]=male, [1]=female

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5)
            print("🔍 Recognizing...")
            query = r.recognize_google(audio)
            print(f"🗣️ You said: {query}")
        except:
            speak("Sorry, I didn't catch that. Type your command.")
            query = input("Command: ")
    return query.lower()

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I'm your AI assistant. How can I help you?")

def run_ai():
    greet()
    while True:
        query = take_command()

        # Basic commands
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            try:
                result = wikipedia.summary(query.replace("wikipedia", ""), sentences=2)
                speak(result)
            except:
                speak("Sorry, I couldn't find that.")

        elif "play" in query:
            song = query.replace("play", "")
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")

        elif "open google" in query:
            webbrowser.open("https://www.google.com")
        elif "open chatgpt" in query:
            webbrowser.open("https://chat.openai.com")
        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com")

        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")

        elif "exit" in query or "stop" in query:
            speak("Goodbye! Have a great day!")
            break

        else:
            speak("I can search Wikipedia, play music, open websites, or tell time. Try saying something like 'play Believer on YouTube'.")

# Run the assistant
if __name__ == "__main__":
    run_ai()
