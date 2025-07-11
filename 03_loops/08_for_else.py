staff = [("Amit", 16), ("Bob", 20), ("Charlie", 18)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to vote")
        break
else:
    print("All staff members have been checked for voting eligibility.")