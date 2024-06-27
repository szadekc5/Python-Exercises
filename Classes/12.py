class Student:
    school = 'WSB Merito'
    address = 'Prosta 4, Warszawa' 
student1 = Student()
student2 = Student() 
student1.student_id = "162605"
student1.student_name = "Bartosz Szadkowski"
student2.student_id = "162605"
student2.marks_language = 80
student2.marks_science = 100
student2.marks_math = 75 
students = [student1, student2]
for student in students:
    print('\n')
    for attr in student.__dict__:
        print(f'{attr} -> {getattr(student, attr)}')
