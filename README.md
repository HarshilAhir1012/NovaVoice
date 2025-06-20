# NovaVoice
Innova Voice Assistant A lightweight Python voice assistant that listens for the wake word "Innova" and performs tasks like playing YouTube videos, telling the time, searching Google, opening websites/apps, and saving reminders — all via simple voice commands with a user-friendly GUI.
# Innova Voice Assistant

Innova is a simple, customizable Python-based voice assistant designed to make your everyday tasks easier with voice commands. Powered by speech recognition and text-to-speech technology, Innova can listen for your commands, respond with speech, play YouTube videos, open websites or applications, tell the current time, and save reminders — all hands-free!

---

## Features

- **Wake word detection:** Say “Innova” to activate the assistant and start issuing commands.  
- **Play YouTube videos and songs:** Just say “play [song or video name]” and Innova will open it on YouTube.  
- **Get the current time:** Ask “what is the time” and Innova will respond with the current local time.  
- **Web search:** Say “search for [query]” to quickly search Google via your default browser.  
- **Open websites and apps:** Launch popular sites like YouTube, Google, GitHub, or apps like Notepad, Calculator, Chrome, and VS Code by voice.  
- **Save reminders and notes:** Tell Innova to “remind me to [task]” or “note that [note]” to save important info to a text file.  
- **Command logging:** All commands you give are saved to a log file for later review or debugging.  
- **GUI interface:** Simple graphical interface with start and stop buttons and status updates.

---

## Installation & Setup

### Requirements

- Python 3.6 or higher installed on your system  
- Microphone connected and configured properly  
- The following Python packages (install via pip):

```bash
pip install speechrecognition pyttsx3 pywhatkit
Note: tkinter comes pre-installed with most Python distributions. If not, install it using your OS package manager.
How to Run
Download or clone this repository:

bash
Copy code
git clone https://github.com/yourusername/innova-voice-assistant.git
cd innova-voice-assistant
Run the main script:

bash
Copy code
python innova_assistant.py
Click Start Listening in the GUI window.

Say "Innova" to activate the assistant.

Speak your commands like:

“Play Shape of You on YouTube”

“What is the time?”

“Search for Python tutorials”

“Open GitHub”

“Remind me to call mom”

“Note that project deadline is tomorrow”

To stop the assistant, say “stop” or click Stop button.

How It Works
The program continuously listens through your microphone for the wake word “Innova”.

When heard, it listens for a follow-up command.

The command is parsed and processed by predefined functions to perform actions.

Feedback is given through speech and text on the GUI.

Commands and reminders are saved in local text files for your reference.

File Structure
innova_assistant.py — main Python script with all voice assistant logic and GUI

reminders.txt — text file storing reminders and notes

commands_log.txt — text file logging all voice commands received

Customization
You can add or modify commands inside the listen_loop function.

Change wake word by updating the keyword check (if "innova" in text:).

Enhance responses by integrating AI or other APIs.

Customize GUI appearance by editing the Tkinter code.

Troubleshooting
Make sure your microphone is connected and set as default input device.

Ensure internet connection is active for commands like playing YouTube or searching Google.

If speech recognition fails, try speaking clearly or in a quieter environment.

For permission errors, run the script as administrator or check mic permissions.

License
This project is open-source and free to use under the MIT License.

Acknowledgments
Uses SpeechRecognition for voice input

Uses pyttsx3 for text-to-speech

Uses pywhatkit for playing YouTube videos

GUI created with Python’s built-in Tkinter

Contact
For questions, suggestions, or contributions, feel free to open an issue or pull request on this repository.

Thank you for checking out Innova!
Happy coding and voice commanding! 🎙️✨