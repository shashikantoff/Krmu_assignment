# ============================================================
# Name: Shashi Kant
# Course: MCA (AI & ML)
# Subject: Programming for Problem Solving Using Python
# Semester: I
# Assignment 01 – Attendance Tracker
# Faculty: Ms. Neha Kaushik
# Date: 12-Nov-2025
# ============================================================

# Importing module
from datetime import datetime

# Welcome message
print("\n------------------------------------------")
print(" Welcome to Python Attendance Tracker Tool ")
print("------------------------------------------")
print("This tool helps record student attendance with timestamps.\n")

# Task 1 & 2: Setup and Data Collection
attendance = {}

# Ask how many students to record
try:
    num_entries = int(input("Enter the number of students to record attendance for: "))
except ValueError:
    print("Invalid input! Please enter a number.")
    exit()

for i in range(num_entries):
    print(f"\n--- Entry {i + 1} ---")

    # Input student name with validation
    name = input("Enter student name: ").strip()
    if not name:
        print("⚠️ Name cannot be empty. Please try again.")
        continue

    # Check for duplicates
    if name in attendance:
        print("⚠️ Duplicate entry! This student is already marked present.")
        continue

    # Input check-in time with validation
    check_in = input("Enter check-in time (e.g., 09:15 AM): ").strip()
    if not check_in:
        print("⚠️ Time cannot be empty. Please re-enter.")
        continue

    # Store in dictionary
    attendance[name] = check_in

# Task 4: Display Attendance Summary
print("\n\n=========== Attendance Summary ===========")
print("Student Name\t\tCheck-in Time")
print("------------------------------------------")

for name, time in attendance.items():
    print(f"{name:20}\t{time}")

print("------------------------------------------")
print(f"Total Students Present: {len(attendance)}")

# Task 5: Absentee Validation (Optional)
choice_absent = input("\nDo you want to calculate absentees? (yes/no): ").lower()
if choice_absent == "yes" or "y":
    try:
        total_students = int(input("Enter total number of students in class: "))
        absentees = total_students - len(attendance)
        if absentees < 0:
            absentees = 0
        print(f"Total Present: {len(attendance)}")
        print(f"Total Absent : {absentees}")
    except ValueError:
        print("Invalid input for total students!")

# Task 6 (Bonus): Save to File
choice_save = input("\nDo you want to save this record to a file? (yes/no): ").lower()

if choice_save == "yes" or "y":
    with open("attendance_log.txt", "w") as file:
        file.write("=========== Attendance Report ===========\n")
        file.write("Student Name\t\tCheck-in Time\n")
        file.write("------------------------------------------\n")
        for name, time in attendance.items():
            file.write(f"{name:20}\t{time}\n")
        file.write("------------------------------------------\n")
        file.write(f"Total Present: {len(attendance)}\n")
        current_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")
        file.write(f"Report Generated On: {current_time}\n")
    print("✅ Attendance report saved as 'attendance_log.txt'.")
else:
    print("📋 Report not saved.")

print("\nThank you for using the Attendance Tracker Tool!")
print("===============================================\n")
