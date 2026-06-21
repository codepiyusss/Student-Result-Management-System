
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

    def percentage(self):
        total = sum(self.marks.values())
        return total / len(self.marks)
    
    