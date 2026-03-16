from grade_tracker.models import Student


def average(values: list[float]) -> float:
    """Calculate the average of a list of values.
    Returns 0.0 if the list is empty."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def subject_average(student: Student, subject: str) -> float:
    """Calculate the average grade of a student for a specific subject."""
    grades = student.grades_for(subject)
    return average([g.value for g in grades])


def overall_average(student: Student) -> float:
    """Calculate the overall average grade of a student across all subjects."""
    return average([g.value for g in student.grades])


def classify(avg: float) -> str:
    """Classify a student based on their average grade.
    90+  -> Excellent
    80+  -> Good
    70+  -> Average
    60+  -> Sufficient
    <60  -> Failed"""
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