"""
 Challenge: Daily Learning Journal Logger

Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.txt` file along with a timestamp.

Your program should:
1. Ask the user what they learned today.
2. Add the entry to a file called `learning_journal.txt`.
3. Each entry should include the date and time it was written.
4. The journal should **append** new entries rather than overwrite.

Bonus:
- Add an optional rating (1-5) for how productive the day was.
- Show a confirmation message after saving the entry.
- Make sure the format is clean and easy to read when opening the file.

Example:
📅 2025-06-14 — 10:45 AM
Today I learned about how list comprehensions work in Python!
Productivity Rating: 4/5
"""

import datetime

entry = input("What did you learn today? ").strip()
rating = input("How productive was your day? (1-5): ").strip()

today = datetime.datetime.now()
formatted_date = today.strftime("%Y-%m-%d - %I:%M %p")

journal_entry = f"📅 {formatted_date}\n{entry}"

if rating:
    journal_entry += f"\nProductivity Rating: {rating}/5"

journal_entry += "\n" + "-" * 50 + "\n"


with open("learning_journal.txt", "a", encoding="utf-8") as file:
    file.write(journal_entry)