class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)

students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        student = Student(roll_no, name, marks)
        students.append(student)

        print("Student added successfully!")

    elif choice == "2":
        for student in students:
            student.display()
            print("--------------------")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
