from student_manager import StudentManager

manager = StudentManager()

while True:

    print("\n Student Management System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        roll = int(input("Enter Roll: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        manager.add_student(roll, name, marks)

    elif choice == "2":
        manager.display_students()

    elif choice == "3":

        roll = int(input("Enter Roll to search: "))
        manager.search_student(roll)

    elif choice == "4":

        roll = int(input("Enter Roll to update: "))
        manager.update_student(roll)

    elif choice == "5":

        roll = int(input("Enter Roll to delete: "))
        manager.delete_student(roll)

    elif choice == "6":

        print("Exiting program")
        break

    else:

        print("Invalid choice")