
class Student:
    id = 0
    name = "noName"
    grade = 1
    score = 50

    def __init__(self):
        self.id = 0

    def to_string(self):
        return '학번 "{}"이고 이름은 "{}" 학년은"{}" 점수는 "{}"'\
            .format(self.id,self.name,self.grade,self.score)

    def print_info(self):
        print(self.to_string())

    def __str__(self):
        return '학번 "{}"이고 이름은 "{}" 학년은"{}" 점수는 "{}"' \
            .format(self.id, self.name, self.grade, self.score)

    def __add__(self, other):
        return other + self.score
