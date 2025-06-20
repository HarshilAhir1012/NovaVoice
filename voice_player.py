import tkinter as tk
from threading import Thread
import speech_recognition as sr
import pywhatkit
import pyttsx3
import datetime
import webbrowser
import os
import subprocess

# ==== INIT SETUP ====
listener = sr.Recognizer()
engine = pyttsx3.init()
listening = False

REMINDERS_FILE = "reminders.txt"
LOG_FILE = "commands_log.txt"

def talk(text):
    engine.say(text)
    engine.runAndWait()

def save_reminder(text):
    with open(REMINDERS_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - {text}\n")

def save_command_log(command):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - {command}\n")

def listen_loop(output_text):
    global listening
    listening = True
    talk("Innova is ready. Say 'Innova' to start.")

    while listening:
        try:
            with sr.Microphone() as source:
                output_text.set("🎤 Waiting for wake word 'Innova'...")
                voice = listener.listen(source)
                text = listener.recognize_google(voice).lower()
                print(f"[RAW] Heard: {text}")

                if "innova" in text:
                    talk("Yes, how can I help you?")
                    output_text.set("🗣 Listening for command...")

                    voice2 = listener.listen(source)
                    command = listener.recognize_google(voice2).lower()
                    print(f"[COMMAND] {command}")
                    output_text.set(f"🗣 You said: {command}")
                    save_command_log(command)

                    if 'stop' in command:
                        talk("Stopping voice assistant. Goodbye!")
                        output_text.set("👋 Assistant stopped.")
                        listening = False
                        break

                    elif 'play' in command:
                        song = command.replace('play', '').strip()
                        talk(f"Playing {song}")
                        output_text.set(f"🎶 Playing: {song}")
                        pywhatkit.playonyt(song)

                    elif 'time' in command:
                        time = datetime.datetime.now().strftime('%I:%M %p')
                        talk(f"The time is {time}")
                        output_text.set(f"⏰ The time is {time}")

                    elif 'search for' in command:
                        query = command.replace('search for', '').strip()
                        talk(f"Searching for {query}")
                        output_text.set(f"🔍 Searching: {query}")
                        webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")

                    elif 'open google' in command:
                        talk("Opening Google")
                        output_text.set("🌐 Opening Google")
                        webbrowser.open("https://www.google.com")

                    elif 'open' in command:
                        site = command.replace('open', '').strip().lower()
                        websites = {
                            "youtube": "https://www.youtube.com",
                            "instagram": "https://www.instagram.com",
                            "facebook": "https://www.facebook.com",
                            "github": "https://www.github.com",
                            "google": "https://www.google.com",
                            "chatgpt": "https://chat.openai.com"
                        }
                        apps = {
                            "notepad": lambda: os.system("start notepad"),
                            "calculator": lambda: os.system("start calc"),
                            "chrome": lambda: subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"),
                            "vs code": lambda: subprocess.Popen("code")
                        }

                        if site in websites:
                            talk(f"Opening {site}")
                            output_text.set(f"🌐 Opening {site}")
                            webbrowser.open(websites[site])
                        elif site in apps:
                            talk(f"Opening {site}")
                            output_text.set(f"💻 Opening {site}")
                            apps[site]()
                        else:
                            talk(f"I don't know {site}, searching it on Google.")
                            output_text.set(f"❓ Unknown site: {site}")
                            webbrowser.open(f"https://www.google.com/search?q={site}")

                    elif command.startswith("remind me to"):
                        reminder_text = command.replace("remind me to", "").strip()
                        save_reminder(reminder_text)
                        talk(f"Reminder saved: {reminder_text}")
                        output_text.set(f"📝 Reminder saved: {reminder_text}")

                    elif command.startswith("note that"):
                        note_text = command.replace("note that", "").strip()
                        save_reminder(note_text)
                        talk(f"Note saved: {note_text}")
                        output_text.set(f"📝 Note saved: {note_text}")

                    else:
                        talk("Sorry, I don't know how to help with that yet.")
                        output_text.set("🤖 No response available for that command.")

                else:
                    output_text.set("⏸ Waiting for wake word 'Innova'...")

        except Exception as e:
            talk("Sorry, I didn't catch that.")
            output_text.set(f"⚠️ Error: {e}")
            print(f"⚠️ Error: {e}")

# ==== GUI SETUP ====

def start_listening(output_text):
    thread = Thread(target=listen_loop, args=(output_text,), daemon=True)
    thread.start()

def stop_listening():
    global listening
    listening = False

root = tk.Tk()
root.title("🧠 Innova Assistant")
root.geometry("420x270")

output_text = tk.StringVar()
output_text.set("Click Start and say 'Innova' to begin")

label = tk.Label(root, textvariable=output_text, wraplength=380, font=("Helvetica", 12))
label.pack(pady=20)

start_button = tk.Button(root, text="🎙️ Start Listening", font=("Helvetica", 12), command=lambda: start_listening(output_text))
start_button.pack(pady=10)

stop_button = tk.Button(root, text="🛑 Stop", font=("Helvetica", 12), command=stop_listening)
stop_button.pack()

root.mainloop()
