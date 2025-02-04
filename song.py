import sys
import time

# Adjusted delays to better match the song's rhythm
delays = [1.2, 1.0, 1.5, 3.2, 1.2, 2.8, 1.4, 1.8, 1.1, 1.5, 1.8]

# Lyrics and their respective character delays
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

# Print with delays for a typewriter effect
for i, (line, char_delay) in enumerate(lines):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(char_delay)  # Delay for each character

    time.sleep(delays[i])  # Line delay after each full line
    print()  # Newline after each line
