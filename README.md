# git-pulse-check

Automate your daily stand-up preparation. This tool extracts your recent work from the local git history and organizes it by author.

## Installation

1. Ensure you have Python 3 and Git installed.
2. Save the code as `pulse.py`.

## Usage

Run the script inside any directory that is a Git repository:

```bash
python pulse.py --days 1
```

## Options

- `--days`: Specify how many days of history to retrieve (default is 1).

## Example Output

```text
--- Git Pulse Report (3 Commits) ---

User: Jane Doe
  - [a1b2c3d] fix: resolve memory leak in worker
  - [e5f6g7h] feat: add authentication middleware

User: John Smith
  - [i9j0k1l] docs: update readme with installation steps
```