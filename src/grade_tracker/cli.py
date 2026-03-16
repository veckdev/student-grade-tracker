from __future__ import annotations

import argparse
import sys

from grade_tracker.calculator import classify, overall_average, subject_average
from grade_tracker.models import Grade, Student
from grade_tracker.repository import load, save


def get_parser() -> argparse.ArgumentParser:
    """Build and return the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="grade_tracker",
        description="Track student grades from the command line.",
    )
    subparsers = parser.add_subparsers(dest="command")

    p_add_student = subparsers.add_parser("add_student", help="Add a new student.")
    p_add_student.add_argument("name", type=str)
    p_add_student.add_argument("student_id", type=str)

    p_add_grade = subparsers.add_parser("add_grade", help="Add a grade to a student.")
    p_add_grade.add_argument("student_id", type=str)
    p_add_grade.add_argument("subject", type=str)
    p_add_grade.add_argument("value", type=float)

    p_report = subparsers.add_parser("report", help="Show a student's report.")
    p_report.add_argument("student_id", type=str)

    subparsers.add_parser("list", help="List all students.")

    return parser


def main() -> None:
    """Entry point for the CLI."""
    parser = get_parser()
    args = parser.parse_args()
    students = load()

    if args.command == "add_student":
        for s in students:
            if s.student_id == args.student_id:
                print(f"Student with ID '{args.student_id}' already exists.")
                sys.exit(1)
        students.append(Student(name=args.name, student_id=args.student_id))
        save(students)
        print(f"Student '{args.name}' added successfully.")

    elif args.command == "add_grade":
        for s in students:
            if s.student_id == args.student_id:
                s.add_grade(Grade(subject=args.subject, value=args.value))
                save(students)
                print(f"Grade {args.value} added to '{args.student_id}' in '{args.subject}'.")
                sys.exit(0)
        print(f"Student with ID '{args.student_id}' not found.")
        sys.exit(1)

    elif args.command == "report":
        for s in students:
            if s.student_id == args.student_id:
                print(f"\nReport for {s.name} (ID: {s.student_id}):")
                print("-" * 40)
                for subject in s.subjects:
                    avg = subject_average(s, subject)
                    print(f"  {subject}: {avg:.1f} ({classify(avg)})")
                print("-" * 40)
                total = overall_average(s)
                print(f"  Overall Average: {total:.1f} ({classify(total)})")
                sys.exit(0)
        print(f"Student with ID '{args.student_id}' not found.")
        sys.exit(1)

    elif args.command == "list":
        if not students:
            print("No students found.")
            sys.exit(0)
        print("\nRegistered Students:")
        for s in students:
            total = overall_average(s)
            print(f"  {s.student_id} - {s.name} | Overall: {total:.1f} ({classify(total)})")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()