import json
from student import Student

students = []


def load_data():
    global students

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

            for item in data:
                student = Student(
                    item["roll_no"],
                    item["name"]
                )

                student.marks = item["marks"]

                students.append(student)

    except FileNotFoundError:
        pass


def save_data():
    data = [student.to_dict() for student in students]

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Data saved successfully.")


def add_student():
    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")

    student = Student(roll_no, name)

    n = int(input("Number of Subjects: "))

    for _ in range(n):
        subject = input("Subject Name: ")
        marks = float(input("Marks: "))
        student.add_marks(subject, marks)

    students.append(student)

    print("Student Added Successfully.")

def view_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print("-" * 30)
        print("Roll No:", student.roll_no)
        print("Name:", student.name)
        print("Percentage:", round(student.percentage(), 2))
        print("Grade:", student.grade())


def search_student():
    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student.roll_no == roll:
            student.report_card()
            return

    print("Student Not Found.")


def rank_students():
    if not students:
        print("No students available.")
        return

    ranked = sorted(
        students,
        key=lambda s: s.percentage(),
        reverse=True
    )

    print("\nSTUDENT RANKINGS")

    for rank, student in enumerate(ranked, start=1):
        print(
            f"{rank}. {student.name} "
            f"({student.percentage():.2f}%)"
        )



load_data()

while True:
    print("\n" + "=" * 40)
    print("STUDENT RESULT MANAGEMENT SYSTEM")
    print("=" * 40)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Show Rankings")
    print("5. Save Data")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        rank_students()

    elif choice == "5":
        save_data()

    elif choice == "6":
        save_data()
        print("Goodbye!")
        break

    else:
        print("Invalid Choice.")
