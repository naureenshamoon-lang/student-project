import json
from pathlib import Path

from student_app.config import APP_NAME, DEBUG, MAX_STUDENTS
from student_app.logger import logger
from student_app.models.student import Student
from student_app.reports.student_report import display_report
from student_app.services.calculator import calculate_grade
from student_app.utils.validation import validate_name, validate_marks

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "student.json"


def load_student():
    """Read the saved student record from data/student.json."""
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def get_name():
    name = input("Enter student name: ").strip()
    if not validate_name(name):
        logger.warning("Empty student name entered")
        print("Error: Name cannot be empty.")
        return None
    return name


def get_marks():
    try:
        marks = int(input("Enter student marks: "))
    except ValueError:
        logger.error("Invalid marks entered: not a number")
        print("Error: Marks must be a number.")
        return None

    if not validate_marks(marks):
        logger.warning(f"Invalid marks entered: {marks}")
        print("Error: Marks must be between 0 and 100.")
        return None
    return marks


def main():
    logger.info("Application started")
    print(f"Starting: {APP_NAME}")
    print(f"Debug Mode: {DEBUG}")
    print(f"Maximum Students: {MAX_STUDENTS}")
    print()

    saved = load_student()
    print("Saved Student (from data/student.json)")
    print("-------------------")
    print(f"ID: {saved['id']}")
    print(f"Name: {saved['name']}")
    print(f"Program: {saved['program']}")
    print(f"Semester: {saved['semester']}")
    print(f"Marks: {saved['marks']}")
    print()

    name = get_name()
    if name is None:
        return

    marks = get_marks()
    if marks is None:
        return

    grade = calculate_grade(marks)
    student = Student(name, marks, grade)
    logger.info(f"Report generated for {name}")
    display_report(student)


if __name__ == "__main__":
    main()