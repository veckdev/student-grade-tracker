# Student Grade Tracker

A command-line tool to track student grades, calculate averages, and generate reports.

## Requirements

- Python 3.11+

## Installation
```bash
git clone https://github.com/veckdev/student-grade-tracker.git
cd student-grade-tracker
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Usage

### Add a student
```bash
python3 -m grade_tracker add_student "Victor Silva" "V001"
```

### Add a grade
```bash
python3 -m grade_tracker add_grade "V001" "Math" 85.0
```

### View a student's report
```bash
python3 -m grade_tracker report "V001"
```

### List all students
```bash
python3 -m grade_tracker list
```

## Grading Scale

| Average | Classification |
|---------|---------------|
| 90–100  | Excellent      |
| 80–89   | Good           |
| 70–79   | Average        |
| 60–69   | Sufficient     |
| 0–59    | Failed         |

## Project Structure
```
src/grade_tracker/
├── models.py       # Data models: Student and Grade
├── calculator.py   # Grade calculations and classification
├── repository.py   # JSON persistence
└── cli.py          # Command-line interface

tests/
├── test_models.py
├── test_calculator.py
├── test_repository.py
└── test_cli.py
```

## Running Tests
```bash
pytest
```

## License

MIT