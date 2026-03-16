import pytest
from grade_tracker.models import Grade, Student
from grade_tracker.repository import save, load


@pytest.fixture
def tmp_path_json(tmp_path):
    return tmp_path / "test_data.json"


@pytest.fixture
def student():
    s = Student(name="Victor da Silva", student_id="V001")
    s.add_grade(Grade(subject="Math", value=85.0))
    s.add_grade(Grade(subject="History", value=70.0))
    return s


class TestRepository:

    def test_save_and_load(self, student, tmp_path_json):
        save([student], path=tmp_path_json)
        result = load(path=tmp_path_json)
        assert len(result) == 1
        assert result[0].name == "Victor da Silva"
        assert result[0].student_id == "V001"
    def test_load_returns_empty_list_if_file_does_not_exist(self, tmp_path_json):
        result = load(path=tmp_path_json)
        assert result == []

    def test_grades_are_preserved_after_save_and_load(self, student, tmp_path_json):
        save([student], path=tmp_path_json)
        result = load(path=tmp_path_json)
        assert len(result[0].grades) == 2
        assert result[0].grades[0].subject == "Math"
        assert result[0].grades[0].value == 85.0