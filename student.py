
class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.marks = {}

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def display(self):
        print(self.roll_no)
        print(self.name)
        print(self.marks)