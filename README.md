# Password Strength Checker (CLI)

A Python CLI tool that analyzes password strength using length, character classes, entropy estimation, and common pattern detection. Provides actionable suggestions to improve security.

## Features
- Checks password length, lowercase/uppercase letters, digits, and symbols
- Detects common passwords and dictionary words
- Detects repeated characters and sequential patterns
- Estimates entropy in bits
- Provides suggestions to improve password strength

## Usage
Interactive:
python pw_checker.py

yaml


Direct password:
python pw_checker.py P@ssw0rd123
... (Your existing Usage section) ...
## Usage
Interactive:
python pw_checker.py

yaml

Direct password:
python pw_checker.py P@sswOrd123

--- (Insert the new section here) ---

## 🛠️ Development Challenges
- **`NameError` Issues:** Resolved function calling errors by ensuring all functions (`analyze`, `pretty_print`, etc.) were defined *before* they were called, enforcing correct Python structure.
- **Dynamic Input:** Implemented the built-in `sys` module to allow the script to accept a specific filename (e.g., `list.txt`) directly from the command line instead of using hardcoded names.
- **File Reading:** Ensured robust file handling using `.strip()` to correctly process passwords from text files by removing invisible newline characters (`\n`).

--- (End of new section) ---

## Screenshot
![Example Output]
[def: password_analysis_screenshot.png]

## Screenshot
![Example Output]


[def]: password_analysis_screenshot.png.png 
