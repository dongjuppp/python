from student import Student
class School:
    def __init__(self):
        self.name = 'noName'
        self.many = 50

    def __add__(self, other):
        return self.many + other
