class Student:
    student_id = '162605'
    student_name = 'Bartosz Szadkowski'
    def display():
        print(f'Student id: {Student.student_id}\nStudent Name: {Student.student_name}')
print("Original attributes and their values of the Student class:")
Student.display()
