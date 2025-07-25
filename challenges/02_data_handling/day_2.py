"""
 Challenge: Student Marks Analyzer

Create a Python program that allows a user to input student names along with their marks and then calculates useful statistics.

Your program should:
1. Let the user input multiple students with their marks (name + integer score).
2. After input is complete, display:
   - Average marks
   - Highest marks and student(s) who scored it
   - Lowest marks and student(s) who scored it
   - Total number of students

Bonus:
- Allow the user to enter all data first, then view the report
- Format output clearly in a report-style layout
- Prevent duplicate student names
"""


def collect_student_details():
    students = {}

    while True:
        name = input("Enter student name (or 'done' to finish): ").strip()
        if name.lower() == "done":
            break

        if name in students:
            print(f"Student {name} already exists. Please enter a different name.")
            continue

        try:
            marks = float(input(f"Enter marks for {name}: ").strip())
            students[name] = marks
        except ValueError:
            print("Invalid marks. Please enter a numeric value.")

    return students

def display_report(students):
    if not students:
        print("No student data available.")
        return
    
    students_marks = students.values()
    max_marks = max(students_marks)
    min_marks = min(students_marks)
    average_marks = sum(students_marks) / len(students_marks)

    toppers = [name for name, marks in students.items() if marks == max_marks]
    lowest_scorers = [name for name, marks in students.items() if marks == min_marks]

    print("\n--- Student Marks Report 🗒️ ---")
    print("-" * 30)
    print(f"Total Students: {len(students)}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Highest Marks: {max_marks} (Achieved by: {', '.join(toppers)})")
    print(f"Lowest Marks: {min_marks} (Achieved by: {', '.join(lowest_scorers)})")
    
    print("-" * 30)
    print("Student Details:")
    for name, marks in students.items():
        print(f"- {name}: {marks}")

def main():
    print("Welcome to the Student Marks Analyzer! 🎓")
    students = collect_student_details()
    display_report(students)

if __name__ == "__main__":
    main()
