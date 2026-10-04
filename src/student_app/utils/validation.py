def validate_name(name):
    return isinstance(name, str) and name.strip() != ""


def validate_marks(marks):
    return 0 <= marks <= 100