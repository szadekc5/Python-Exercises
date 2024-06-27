def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: $ {kwargs['student_name']}")
    
    if 'student_name' and 'student_group_number' in kwargs:
            print(f"\nStudent Name: $ {kwargs['student_name']}")
            print(f"Student Class: $ {kwargs['student_group_number']}")

 
student_data(student_id='SV12', student_name='Bartosz Szadkowski')

student_data(student_id='SV12', student_name='Bartosz Szadkowski', student_class ='13')
