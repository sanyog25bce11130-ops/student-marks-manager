# Student Marks Manager
# Very simple Python project using only lists and basic functions

students = []
marks = []

def add_student():
    name = input("Enter student name: ")
    score = int(input("Enter marks: "))

    students.append(name)
    marks.append(score)

    print("Student added successfully.\n")

def show_all():
    if len(students) == 0:
        print("No student data available.\n")
        return

    print("\n--- All Students ---")
    for i in range(len(students)):
        print(students[i], "-", marks[i])
    print()

def search_student():
    name = input("Enter student name to search: ")

    found = False
    for i in range(len(students)):
        if students[i].lower() == name.lower():
            print("Marks of", students[i], "=", marks[i], "\n")
            found = True
            break

    if not found:
        print("Student not found.\n")

def highest_marks():
    if len(marks) == 0:
        print("No data available.\n")
        return

    max_marks = max(marks)
    index = marks.index(max_marks)

    print("Topper:", students[index], "with", max_marks, "marks.\n")

def average_marks():
    if len(marks) == 0:
        print("No data available.\n")
        return

    avg = sum(marks) / len(marks)
    print("Class Average =", round(avg, 2), "\n")

def menu():
    while True:
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("4. Highest Marks")
        print("5. Average Marks")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_all()
        elif choice == "3":
            search_student()
        elif choice == "4":
            highest_marks()
        elif choice == "5":
            average_marks()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.\n")

menu()
