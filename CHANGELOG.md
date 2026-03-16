# Changelog

All notable changes to this project will be documented in this file.

## [0.2.0] - 2026-03-16

### Changed
- Replaced CLI commands with an interactive menu
- Menu options: Add student, Add grade, View report, List students, Exit
- Input validation with retry on invalid entries

## [0.1.0] - 2026-03-16

### Added
- `Grade` model with validation (0–100 scale)
- `Student` model with grade management
- Grade calculations: subject average, overall average
- Classification system: Excellent, Good, Average, Sufficient, Failed
- JSON persistence with save and load
- Interactive CLI menu
- Unit tests for all modules (29 tests)
- `README.md`, `LICENSE` and `CHANGELOG.md`