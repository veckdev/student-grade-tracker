from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from grade_tracker.models import Grade, Student

DEFAULT_PATH = Path("data/data.json")


def save(students: list[Student], path: Path = DEFAULT_PATH) -> None:
    """Save a list of students to a JSON file on disk."""
    path.parent.mkdir(parents=True, exist_ok=True)
    data = [_student_to_dict(s) for s in students]
    path.write_text(json.dumps(data, indent=2))


def load(path: Path = DEFAULT_PATH) -> list[Student]:
    """Read the JSON file and return the list of students.
    Returns an empty list if the file does not exist."""
    if not path.exists():
        return []
    data = json.loads(path.read_text())
    return [_student_from_dict(s) for s in data]


def _student_to_dict(student: Student) -> dict:
    """Convert a Student object into a dictionary so it can be saved as JSON."""
    return {
        "name": student.name,
        "student_id": student.student_id,
        "grades": [_grade_to_dict(g) for g in student.grades],
    }


def _grade_to_dict(grade: Grade) -> dict:
    """Convert a Grade object into a dictionary so it can be saved as JSON."""
    return {
        "subject": grade.subject,
        "value": grade.value,
        "date": grade.date.isoformat(),
    }


def _student_from_dict(data: dict) -> Student:
    """Convert a dictionary read from JSON back into a Student object."""
    student = Student(name=data["name"], student_id=data["student_id"])
    for g in data["grades"]:
        student.add_grade(_grade_from_dict(g))
    return student


def _grade_from_dict(data: dict) -> Grade:
    """Convert a dictionary read from JSON back into a Grade object."""
    return Grade(
        subject=data["subject"],
        value=data["value"],
        date=date.fromisoformat(data["date"]),
    )