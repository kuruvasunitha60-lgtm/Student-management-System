students = []

def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    branch = input("Enter Branch: ")
    marks = input("Enter Marks: ")

    student = {
        "Roll Number": roll_no,
        "Name": name,
        "Branch": branch,
        "Marks": marks
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
    else:
        for student in students:
            print(student)

def search_student():
    roll_no = input("Enter Roll Number to search: ")

    for student in students:
        if student["Roll Number"] == roll_no:
            print(student)
            return

    print("Student not found.")

def update_student():
    roll_no = input("Enter Roll Number to update: ")

    for student in students:
        if student["Roll Number"] == roll_no:
            student["Name"] = input("Enter New Name: ")
            student["Branch"] = input("Enter New Branch: ")
            student["Marks"] = input("Enter New Marks: ")
            print("Student updated successfully!")
            return

    print("Student not found.")

def delete_student():
    roll_no = input("Enter Roll Number to delete: ")

    for student in students:
        if student["Roll Number"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")