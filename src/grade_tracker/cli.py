from __future__ import annotations

import sys

from grade_tracker.calculator import classify, overall_average, subject_average
from grade_tracker.models import Grade, Student
from grade_tracker.repository import load, save


def print_menu() -> None:
    """Print the main menu."""
    print("\n=== Grade Tracker ===")
    print("1. Add student")
    print("2. Add grade")
    print("3. View report")
    print("4. List students")
    print("0. Exit")


def get_input(prompt: str) -> str:
    """Get non-empty input from the user."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  This field cannot be empty. Try again.")


def get_float_input(prompt: str, min_val: float, max_val: float) -> float:
    """Get a float input within a valid range."""
    while True:
        try:
            value = float(input(prompt).strip())
            if min_val <= value <= max_val:
                return value
            print(f"  Value must be between {min_val} and {max_val}. Try again.")
        except ValueError:
            print("  Invalid number. Try again.")


def find_student(students: list[Student], student_id: str) -> Student | None:
    """Find a student by ID."""
    for s in students:
        if s.student_id == student_id:
            return s
    return None


def add_student(students: list[Student]) -> None:
    """Prompt user to add a new student."""
    print("\n-- Add Student --")
    while True:
        name = get_input("  Enter student name: ")
        student_id = get_input("  Enter student ID: ")
        if find_student(students, student_id):
            print(f"  Error: ID '{student_id}' already exists. Try again.")
        else:
            students.append(Student(name=name, student_id=student_id))
            save(students)
            print(f"  Student '{name}' added successfully!")
            break


def add_grade(students: list[Student]) -> None:
    """Prompt user to add a grade to a student."""
    print("\n-- Add Grade --")
    while True:
        student_id = get_input("  Enter student ID: ")
        student = find_student(students, student_id)
        if not student:
            print(f"  Error: student '{student_id}' not found. Try again.")
        else:
            break
    subject = get_input("  Enter subject: ")
    value = get_float_input("  Enter grade (0–100): ", 0.0, 100.0)
    student.add_grade(Grade(subject=subject, value=value))
    save(students)
    print(f"  Grade {value} added to '{student.name}' in '{subject}'.")


def view_report(students: list[Student]) -> None:
    """Prompt user to view a student's report."""
    print("\n-- View Report --")
    while True:
        student_id = get_input("  Enter student ID: ")
        student = find_student(students, student_id)
        if not student:
            print(f"  Error: student '{student_id}' not found. Try again.")
        else:
            break
    print(f"\n  Report for {student.name} (ID: {student.student_id})")
    print("  " + "-" * 38)
    if not student.grades:
        print("  No grades yet.")
    else:
        for subject in student.subjects:
            avg = subject_average(student, subject)
            print(f"  {subject}: {avg:.1f} ({classify(avg)})")
        print("  " + "-" * 38)
        total = overall_average(student)
        print(f"  Overall Average: {total:.1f} ({classify(total)})")


def list_students(students: list[Student]) -> None:
    """List all registered students."""
    print("\n-- Students --")
    if not students:
        print("  No students found.")
        return
    for s in students:
        if s.grades:
            total = overall_average(s)
            print(f"  {s.student_id} - {s.name} | Overall: {total:.1f} ({classify(total)})")
        else:
            print(f"  {s.student_id} - {s.name} | No grades yet.")


def main() -> None:
    """Entry point for the interactive menu."""
    students = load()
    while True:
        print_menu()
        choice = input("\nChoose an option: ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            add_grade(students)
        elif choice == "3":
            view_report(students)
        elif choice == "4":
            list_students(students)
        elif choice == "0":
            print("\nGoodbye!")
            sys.exit(0)
        else:
            print("  Invalid option. Try again.")


if __name__ == "__main__":
    main()