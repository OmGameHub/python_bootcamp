"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""

import time

while True:
    try:
        seconds = int(input("⏰ Enter the time in seconds: "))
        if seconds < 1:
            print("Please enter a number greater than 0")
            continue
        break
    except ValueError:
        print("Invalid input, please enter a whole number")

print()
print("🔔 Timer started...")
for remaining in range(seconds, 0, -1):
    mins, secs = divmod(remaining, 60)
    time_format = f"{mins:02}:{secs:02}"
    print(f"⏳ Time left: {time_format}", end="\r")
    time.sleep(1)

print("\n")
print("⌛️ Time's up! Take a break or move on to next task.")
print("\a")

