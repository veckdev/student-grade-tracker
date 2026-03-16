# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2026-03-16

### Added
- `Grade` model with validation (0–100 scale)
- `Student` model with grade management
- Grade calculations: subject average, overall average
- Classification system: Excellent, Good, Average, Sufficient, Failed
- JSON persistence with save and load
- CLI commands: `add_student`, `add_grade`, `report`, `list`
- Unit tests for all modules (29 tests)