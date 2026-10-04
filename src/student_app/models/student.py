class Student:
    def __init__(self, name, marks, grade):
        self.name = name
        self.marks = marks
        self.grade = grade

    def get_details(self):
        return {
            "name": self.name,
            "marks": self.marks,
            "grade": self.grade,
        }

    def __str__(self):
        return f"{self.name} - {self.marks} marks - Grade {self.grade}"