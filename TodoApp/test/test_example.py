import pytest

class Student:
    def __init__(self, first_name: str, last_name: str, age: int, major: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.major = major

@pytest.fixture
def default_student():
    return Student("bao", "bao", 4, "Marking")

def test_student_initialization(default_student):
    assert default_student.first_name == "bao", "first name should be bao"
    assert default_student.last_name == "bao"
    assert default_student.age == 4
    assert default_student.major == "Marking"