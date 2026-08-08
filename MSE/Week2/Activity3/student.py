
import json
from pathlib import Path

# define a class to represent student information
class StudentInfo:
    def __init__(self, name: str, age: int, student_id: str, address: str = None):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        if self.address:
            print(f"Address: {self.address}")

# load students from json file
def load_students_from_json(file_path: str = None):
    if file_path is None:
        file_path = Path(__file__).with_name("studentsList.json")

    with open(file_path, "r", encoding="utf-8") as handle:
        raw_students = json.load(handle)

    return [StudentInfo(**student_data) for student_data in raw_students]

# display students sorted by age
def display_students(students=None):
    if students is None:
        students = load_students_from_json()

    sorted_students = sorted(students, key=lambda student: student.age)

    print("Sorted Students by Age:")
    for student in sorted_students:
        student.display_info()
        print()


if __name__ == "__main__":
    display_students()
