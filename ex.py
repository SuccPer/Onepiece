class Student(object):
    def __init__(self , name , score):
        self.name = name
        self.score = score

    def print_score(self):
        return ('%s: %d' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
