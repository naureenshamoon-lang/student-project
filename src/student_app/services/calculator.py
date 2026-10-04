def calculate_grade(marks):
    """Return the letter grade for the given marks."""
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

    

def get_status(marks):
    """Return 'Pass' for 50 or more marks, otherwise 'Fail'."""
    return "Pass" if marks >= 50 else "Fail"