from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass
class Grade:
    """Represents a single grade for a subject."""

    subject: str
    value: float
    date: date = field(default_factory=date.today)

    def __post_init__(self) -> None:
        """Validate and clean up fields after initialization."""
        self.subject = self.subject.strip()
        if not self.subject:
            raise ValueError("Subject cannot be empty.")
        if not (0.0 <= self.value <= 100.0):
            raise ValueError(
                f"Grade value must be between 0 and 100. {self.value} is invalid."
            )


@dataclass
class Student:
    """Represents a student with a collection of grades."""

    name: str
    student_id: str
    grades: list[Grade] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Validate and clean up fields after initialization."""
        self.name = self.name.strip()
        self.student_id = self.student_id.strip()
        if not self.name:
            raise ValueError("Student name cannot be empty.")
        if not self.student_id:
            raise ValueError("Student ID cannot be empty.")

    def add_grade(self, grade: Grade) -> None:
        """Add a grade to the student's record."""
        self.grades.append(grade)

    def grades_for(self, subject: str) -> list[Grade]:
        """Return all grades for a given subject (case-insensitive)."""
        return [g for g in self.grades if g.subject.lower() == subject.lower()]

    @property
    def subjects(self) -> list[str]:
        """Return unique subjects in order of first appearance."""
        seen: set[str] = set()
        result: list[str] = []
        for g in self.grades:
            key = g.subject.lower()
            if key not in seen:
                seen.add(key)
                result.append(g.subject)
        return result