# Changelog

All notable changes to the Windfall Engine will be documented in this file.

## [0.2.1] - 2024-05-22
### Added
- Created `windfall/engine/` package structure.
- Introduced `__init__.py` hub (Facade pattern) for centralized imports.
- Added `engine/core/`, `engine/scenes/`, `engine/renderers/`, and `engine/events/` subdirectories.
- Added `migrate_v021.py` and `apply_aliases.py` utility scripts for structural maintenance.

### Changed
- Refactored all internal imports to use the `windfall.engine` alias.
- Moved `WindfallCore` to `engine/core/`.
- Moved `BaseScene`, `SplashScene`, and `MainMenuScene` to `engine/scenes/`.
- Updated `README.md` to use a dynamic version badge.

### Fixed
- Resolved "Detached HEAD" and "Nothing to commit" errors in GitHub Actions.
- Fixed UTF-8 encoding issues when reading files with ASCII art on Windows.

## [0.2.0] - 2024-05-21
### Added
- Created the `updates/` directory and `version.json` for version tracking.
- Implemented `BaseScene` inheritance model for all game scenes.
- Added `SplashScene` with automated transition logic.
- Implemented `MainMenuScene` with basic TUI selection.
- Set up GitHub Actions for automated README version updates.

### Changed
- Standardized the project name to "Windfall Engine".
- Refactored the main entry point to use a class-based `WindfallCore`.

## [0.1.0] - 2024-05-15
### Added
- Initial project setup and repository initialization.
- Basic TUI renderer using standard output.
- Proof-of-concept ASCII art display for the splash screen.
- Rudimentary keyboard input detection.