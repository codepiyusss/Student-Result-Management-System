from student import Student

s1 = Student(101, "Piyush")

s1.add_marks("Math", 90)
s1.add_marks("Physics", 85)

s1.display()

print("Percentage:", s1.percentage())
