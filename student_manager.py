import json

from student import Student
class StudentManager:

    def __init__(self):
        self.students = [] 
        self.load_students()

    def add_student(self, roll, name, marks):
        student = Student(roll, name, marks)
        self.students.append(student)
        self.save_students()
        print("Student added successfully!")

    def display_students(self):

        if len(self.students) == 0:
            print("No students found")
            return

        for s in self.students:
            print(f"Roll: {s.roll}, Name: {s.name}, Marks: {s.marks}")
    def search_student(self, roll):

        for s in self.students:
            if s.roll == roll:
              print(f"Student Found → Roll: {s.roll}, Name: {s.name}, Marks: {s.marks}")
              return

        print("Student not found")

    def update_student(self, roll):

        for s in self.students:

            if s.roll == roll:

             s.name = input("Enter new name: ")
             s.marks = float(input("Enter new marks: "))
             self.save_students()
             print("Student updated successfully!")
             return

        print("Student not found")   

    def delete_student(self, roll):

        for s in self.students:

            if s.roll == roll:
             self.students.remove(s)
             self.safe_students()
             print("Student deleted successfully!")
             return

        
        print("Student not found")  

    def load_students(self):
        try:
            with open('students.json', 'r') as file:
                data = json.load(file)

                for item in data:
                    student = Student.from_dict(item)
                    self.students.append(student)
        except FileNotFoundError:
            pass

    def save_students(self):
        data = []

        for s in self.students:
            data.append(s.to_dict())
    
        with open('students.json', 'w') as file:
            json.dump(data, file, indent=4)