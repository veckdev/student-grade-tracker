import pytest
from grade_tracker.models import Grade, Student
from grade_tracker.calculator import average, subject_average, overall_average, classify


class TestAverage:

    def test_average_of_values(self):
        assert average([80.0, 90.0, 70.0]) == 80.0

    def test_average_returns_zero_for_empty_list(self):
        assert average([]) == 0.0


class TestClassify:

    def test_classify_excellent(self):
        assert classify(90.0) == "Excellent"

    def test_classify_good(self):
        assert classify(85.0) == "Good"

    def test_classify_average(self):
        assert classify(75.0) == "Average"

    def test_classify_sufficient(self):
        assert classify(65.0) == "Sufficient"

    def test_classify_failed(self):
        assert classify(50.0) == "Failed"


class TestStudentAverages:

    def test_subject_average(self):
        s = Student(name="Victor", student_id="V001")
        s.add_grade(Grade(subject="Math", value=80.0))
        s.add_grade(Grade(subject="Math", value=90.0))
        assert subject_average(s, "Math") == 85.0

    def test_overall_average(self):
        s = Student(name="Victor", student_id="V001")
        s.add_grade(Grade(subject="Math", value=80.0))
        s.add_grade(Grade(subject="History", value=60.0))
        assert overall_average(s) == 70.0