class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

    def display(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")