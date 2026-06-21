class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.marks = {}

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def percentage(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def grade(self):
        per = self.percentage()

        if per >= 90:
            return "A+"
        elif per >= 80:
            return "A"
        elif per >= 70:
            return "B"
        elif per >= 60:
            return "C"
        elif per >= 50:
            return "D"
        else:
            return "F"

    def report_card(self):
        print("\n" + "=" * 40)
        print("REPORT CARD")
        print("=" * 40)

        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")

        print("\nMarks:")
        for subject, marks in self.marks.items():
            print(f"{subject}: {marks}")

        print(f"\nPercentage : {self.percentage():.2f}%")
        print(f"Grade      : {self.grade()}")
        print("=" * 40)

    def to_dict(self):
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "marks": self.marks
        }
