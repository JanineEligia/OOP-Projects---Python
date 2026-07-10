# OOP Project #3 : Student Grade Management System

class Student:

    def __init__(self, name, student_id, grade):
        
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def __str__(self):

        return f"{self.name} ({self.student_id}) - {self.grade}"

    def display_info(self):

        print(f"Student Name: {self.name}")
        print(f"Student ID No. {self.student_id}")
        print(f"Grade: {self.grade}")

class Classroom:

    def __init__(self):

        self.students = []

    def add_student(self):

        new_student = input("Enter Name: ")
        id_num = input("Enter Student's ID Number: ")

        try: 

            grade = int(input("Enter Student's Grade: "))

            student = Student(new_student, id_num, grade)
            self.students.append(student)

        except ValueError:

            print("Plz Enter a Numberical Number for a Grade")

    def remove_student(self):

        find_name = input("Enter Student's Name: ")

        for student in self.students:

            if find_name == student.name:

                self.students.remove(student)
                print("Student Successfully Removed")
                
                return
        
        print("This Student is not in the Database")

    def display_students(self):

        for student in self.students:

            print(student)

        if not self.students:

            print("There is currently no students in the database")

    def find_student(self):

        find_id = input("Enter Student's ID Number: ")

        for student in self.students:

            if find_id == student.student_id:

                print(student)
                
                return
        
        print("This Student is not in the Database")

    def change_grade(self):

        student_name = input("Enter Student's Name: ")

        for student in self.students:

            if student_name == student.name:
                
                try: 

                    student.grade = int(input("Enter New Grade: "))
                    print("This Student's Grade has been successfully updated")
                    
                    return
                
                except ValueError:

                    print("Plz Enter a Numberical Number for a Grade")

                    return

        print("This Student is not in the Database")

    def average_grade(self):

        total = 0
        num_of_students = 0 

        for student in self.students:

            total += student.grade
            num_of_students += 1

        try:
            
            average = total/ num_of_students
            print(f"The Average Grade of the Class is {average}")

        except ZeroDivisionError:

            print("There Are No Students in the Database. Plz Enter a Student")

classroom = Classroom()

while True:

    print("===== Classroom =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Display Students")
    print("4. Find Student")
    print("5. Change Grade")
    print("6. Average Grade")
    print("7. Exit")
    print("=====================")

    choice = input("Enter Number of Choosen Operation: ")

    if choice == "1":

        classroom.add_student()

    elif choice == "2":

        classroom.remove_student()

    elif choice == "3":

        classroom.display_students()

    elif choice == "4":

        classroom.find_student()

    elif choice == "5":

        classroom.change_grade()

    elif choice == "6":

        classroom.average_grade()

    elif choice == "7":

        print("Exiting Program....")

        break

    else:

        print("Plz Enter a Valid Number of an Operation in the Menu Above")