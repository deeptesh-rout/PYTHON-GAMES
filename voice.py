import sys
import time
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 140)  # Adjust speech speed
engine.setProperty('volume', 1.0)  # Max volume

# Adjusted delays to match the song’s rhythm
delays = [1.2, 1.0, 1.5, 3.2, 1.2, 2.8, 1.4, 1.8, 1.1, 1.5, 1.8]

# Lyrics and respective character delays
lines = [
    ("Subhaan Allaah Subhaan Allah Subhaan Allah Subhaan Allah", 0.08),
    ("Subhaan Allaah Subhaan Allah Subhaan Allah Subhaan Allah.", 0.1),
    ("Chaand Sifarish Jo Karta Hamari Deta Woh Tumko Bata", 0.12),
    ("Sharm-O-Haya Pe Parde Gira Ke Karni Hain Hamko Khata", 0.15),
    ("Zidd Hain Ab Toh Hain Khud Ko Mitana Hona Hain Tujhmein Fanaa!", 0.08),
    ("Chaand Sifarish Jo Karta Hamari Deta Woh Tumko Bata", 0.12),
    ("Sharm-O-Haya Pe Parde Gira Ke Karni Hain Hamko Khata.", 0.1),
    ("Teri Adaa Bhi Hain Jhonke Wali Chhu Ke Gujar Jaane De", 0.08),
    ("Teri Lachak Hain Ke Jaise Daali Dil Mein Utar Jaane De", 0.1),
    ("Aaja Baahon Mein Karke Bahana Hona Hain Tujhmein Fanaa", 0.12),
    ("Chaand Sifarish Jo Karta Hamari Deta Woh Tumko Bata", 0.12)
]

# Function to type and speak synchronously
def type_and_speak(text, char_delay):
    for char in text:
        print(char, end='', flush=True)
        engine.say(char)  # Speak each character
        time.sleep(char_delay)  # Typing effect
    print()  # New line after each line

# Start the speech engine once
engine.startLoop(False)

# Typing effect + Voice synchronization
for i, (line, char_delay) in enumerate(lines):
    type_and_speak(line, char_delay)
    time.sleep(delays[i])  # Delay between lines

# Ensure speech completes at the end
engine.endLoop()

print("\nPlayback Complete 🎤🎶")
