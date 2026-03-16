import pytest
from grade_tracker.models import Grade, Student


class TestGrade:

    def test_valid_grade_is_created(self):
        g = Grade(subject="Math", value=75.0)
        assert g.subject == "Math"
        assert g.value == 75.0

    def test_strips_whitespace_from_subject(self):
        g = Grade(subject="  Math  ", value=60.0)
        assert g.subject == "Math"

    def test_raises_on_empty_subject(self):
        with pytest.raises(ValueError):
            Grade(subject="", value=50.0)

    def test_raises_when_value_above_100(self):
        with pytest.raises(ValueError):
            Grade(subject="Math", value=101.0)

    def test_raises_when_value_is_negative(self):
        with pytest.raises(ValueError):
            Grade(subject="Math", value=-1.0)
            
            
class TestStudent:

    def test_valid_student_is_created(self):
        s = Student(name="Victor da Silva", student_id="V001")
        assert s.name == "Victor da Silva"
        assert s.grades == []

    def test_raises_on_empty_name(self):
        with pytest.raises(ValueError):
            Student(name="", student_id="V001")

    def test_raises_on_empty_id(self):
        with pytest.raises(ValueError):
            Student(name="Victor", student_id="")

    def test_add_grade(self):
        s = Student(name="Victor", student_id="V001")
        g = Grade(subject="Math", value=85.0)
        s.add_grade(g)
        assert len(s.grades) == 1

    def test_grades_for_filters_by_subject(self):
        s = Student(name="Victor", student_id="V001")
        s.add_grade(Grade(subject="Math", value=80.0))
        s.add_grade(Grade(subject="History", value=70.0))
        s.add_grade(Grade(subject="Math", value=90.0))
        result = s.grades_for("Math")
        assert len(result) == 2
