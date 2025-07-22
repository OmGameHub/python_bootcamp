"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200  
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400  
  Neha owes ₹400  
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""

def get_valid_amount(prompt: str):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter valid amount.")

people_count = int(input("How many people are in the group? "))
people_names = []

for i in range(people_count):
    name = input(f"Enter person's #{i + 1} name: ").strip()
    people_names.append(name)

total_bill = get_valid_amount("Enter the total bill amount in number only: ")
share_per_person = round(total_bill / people_count, 2)

print("\n" + "*" * 40)
print(f"Total bill: {total_bill}")
print(f"Each person owes {share_per_person}")
print()

for person_name in people_names:
    print(f"{person_name} owes ${share_per_person}")

print("\n" + "*" * 40)