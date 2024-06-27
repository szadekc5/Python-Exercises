class Student: 
    def __init__(self, student_id, student_name, group_number):
        self.student_id = student_id
        self.student_name = student_name
        self.gorup_number = group_number 
student = Student('162605', 'Bartosz Szadkowski', '13')
print(student.__dict__)
