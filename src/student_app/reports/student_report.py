def generate_report(student):
    lines = [
        "",
        "Student Report",
        "----------------",
        f"Name: {student.name}",
        f"Marks: {student.marks}",
        f"Grade: {student.grade}",
    ]
    return "\n".join(lines)


def display_report(student):
    print(generate_report(student))