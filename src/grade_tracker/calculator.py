from grade_tracker.models import Student

def average(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)

def subject_average(student: Student, subject: str) -> float:
    grades = student.grades_for(subject)
    return average([g.value for g in grades])

def overall_average(student: Student) -> float:
    return average([g.value for g in student.grades])

def classify(avg: float) -> str:
    if avg >= 90.0:
        return "Excellent"
    elif avg >= 80.0:
        return "Good"
    elif avg >= 70.0:
        return "Average"
    elif avg >= 60.0:
        return "Sufficient"
    else:
        return "Failed"