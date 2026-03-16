import pytest
from pathlib import Path
from grade_tracker.cli import main


@pytest.fixture(autouse=True)
def tmp_data(tmp_path, monkeypatch):
    """Redirect all save/load calls to a temporary file."""
    data_file = tmp_path / "data.json"
    monkeypatch.setattr("grade_tracker.repository.DEFAULT_PATH", data_file)
    monkeypatch.setattr("grade_tracker.cli.load", lambda: __import__("grade_tracker.repository", fromlist=["load"]).load(data_file))
    monkeypatch.setattr("grade_tracker.cli.save", lambda students: __import__("grade_tracker.repository", fromlist=["save"]).save(students, data_file))


def run(args: list[str], capsys):
    """Helper to run CLI commands and capture output."""
    import sys
    sys.argv = ["grade_tracker"] + args
    try:
        main()
    except SystemExit:
        pass
    return capsys.readouterr().out


class TestCLI:

    def test_add_student(self, capsys):
        output = run(["add_student", "Victor Silva", "V001"], capsys)
        assert "Victor Silva" in output

    def test_add_duplicate_student(self, capsys):
        run(["add_student", "Victor Silva", "V001"], capsys)
        output = run(["add_student", "Victor Silva", "V001"], capsys)
        assert "already exists" in output

    def test_add_grade(self, capsys):
        run(["add_student", "Victor Silva", "V001"], capsys)
        output = run(["add_grade", "V001", "Math", "85.0"], capsys)
        assert "85.0" in output

    def test_add_grade_student_not_found(self, capsys):
        output = run(["add_grade", "X999", "Math", "85.0"], capsys)
        assert "not found" in output

    def test_report(self, capsys):
        run(["add_student", "Victor Silva", "V001"], capsys)
        run(["add_grade", "V001", "Math", "85.0"], capsys)
        output = run(["report", "V001"], capsys)
        assert "Victor Silva" in output
        assert "Math" in output
        assert "Overall Average" in output

    def test_list(self, capsys):
        run(["add_student", "Victor Silva", "V001"], capsys)
        output = run(["list"], capsys)
        assert "Victor Silva" in output

    def test_list_empty(self, capsys):
        output = run(["list"], capsys)
        assert "No students found" in output