
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

def test_array():
    my_list = [1, 2, 3, 4, 5, 6]
    my_list[2:5] = [97, 98, 99, 100]
    print(my_list)  # Output: [1, 2, 99, 100, 5]
    print(dir(my_list))  # Output: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

if __name__ == "__main__":
    # display_students()
    test_array()
