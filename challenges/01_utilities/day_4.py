"""
 Challenge: Minutes Alive Calculator

Write a Python script that calculates approximately how many minutes old a person is, based on their age in years.

Your program should:
1. Ask the user for their age in years (accept float values too).
2. Convert that age into:
   - Total days
   - Total hours
   - Total minutes
3. Display the result in a readable format.

Assumptions:
- You can use 365.25 days/year to account for leap years.
- You don't need to handle time zones or exact birthdates in this version.

Example:
Input:
  Age: 25

Output:
  You are approximately:
    - 9,131 days old
    - 219,144 hours old
    - 13,148,640 minutes old

Bonus:
- Add comma formatting for large numbers
- Let the user try again without restarting the program
"""

def calculate_minutes(age_years):
    DAYS_IN_YEAR = 365.25
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60

    total_days = age_years * DAYS_IN_YEAR
    total_hours = total_days * HOURS_IN_DAY
    total_minutes = total_hours * MINUTES_IN_HOUR

    return round(total_days), round(total_hours), round(total_minutes)

while True:
    try:
        age = float(input("Enter youy age in years: "))
        calculate_minutes(age)
        days, hours, minutes = calculate_minutes(age)

        print(f"\nYou are approximately:")
        print(f"- {days:,.0f} days old")
        print(f"- {hours:,.0f} hours old")
        print(f"- {minutes:,.0f} minutes old")

        try_again = input("Do you want to calculate again? (y/n): ").strip().lower()
        if try_again != 'y':
            print("Good bye!")
            break

    except:
        print("Please enter a valid number of age in years.")