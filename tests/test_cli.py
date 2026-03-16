import pytest
from grade_tracker.cli import main
from grade_tracker import repository


@pytest.fixture(autouse=True)
def tmp_data(tmp_path, monkeypatch):
    """Redirect save/load to a temporary file."""
    data_file = tmp_path / "data.json"
    monkeypatch.setattr(repository, "DEFAULT_PATH", data_file)
    monkeypatch.setattr("grade_tracker.cli.load", lambda: repository.load(data_file))
    monkeypatch.setattr("grade_tracker.cli.save", lambda students: repository.save(students, data_file))


def run(inputs: list[str], capsys, monkeypatch):
    """Simulate user typing inputs and run main."""
    inputs_copy = list(inputs)
    monkeypatch.setattr("builtins.input", lambda _: inputs_copy.pop(0))
    try:
        main()
    except (SystemExit, IndexError):
        pass
    return capsys.readouterr().out


class TestCLI:

    def test_add_student(self, capsys, monkeypatch):
        output = run(["1", "Victor Silva", "V001", "0"], capsys, monkeypatch)
        assert "Victor Silva" in output

    def test_add_duplicate_student(self, capsys, monkeypatch):
        run(["1", "Victor Silva", "V001", "0"], capsys, monkeypatch)
        output = run(["1", "Victor Silva", "V001", "Other Name", "V002", "0"], capsys, monkeypatch)
        assert "already exists" in output

    def test_add_grade(self, capsys, monkeypatch):
        run(["1", "Victor Silva", "V001", "0"], capsys, monkeypatch)
        output = run(["2", "V001", "Math", "85.0", "0"], capsys, monkeypatch)
        assert "85.0" in output

    def test_add_grade_student_not_found(self, capsys, monkeypatch):
        output = run(["2", "X999", "V001", "Math", "85.0", "0"], capsys, monkeypatch)
        assert "not found" in output

    def test_report(self, capsys, monkeypatch):
        run(["1", "Victor Silva", "V001", "0"], capsys, monkeypatch)
        run(["2", "V001", "Math", "85.0", "0"], capsys, monkeypatch)
        output = run(["3", "V001", "0"], capsys, monkeypatch)
        assert "Victor Silva" in output
        assert "Math" in output
        assert "Overall Average" in output

    def test_list(self, capsys, monkeypatch):
        run(["1", "Victor Silva", "V001", "0"], capsys, monkeypatch)
        output = run(["4", "0"], capsys, monkeypatch)
        assert "Victor Silva" in output

    def test_list_empty(self, capsys, monkeypatch):
        output = run(["4", "0"], capsys, monkeypatch)
        assert "No students found" in output