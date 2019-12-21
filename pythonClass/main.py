from student import Student
from school import School
dong = Student()
dong.id = 201714031
dong.name = 'dongju'
dong.grade = 3
dong.score = 100
dong.print_info()

kg = School()
kg.many = 99

print(dong)
print(dong+kg)