# Console Quiz Application

A modular terminal-based quiz application built using Python.

## Features

- User registration
- User login
- Profile management
- Profile updates
- Multiple quiz categories
- DSA
- DBMS
- Python
- System Design
- Random question selection
- Randomized answer options
- 30-second timer per question
- Automatic timeout
- Score calculation
- Pass/fail status
- Persistent quiz results
- JSON-based question database

## Project Structure

```text
quiz_application/
│
├── main.py
│
├── data/
│   ├── questions.json
│   ├── users.json
│   └── results.json
│
├── modules/
│   ├── __init__.py
│   ├── auth.py
│   ├── database.py
│   ├── profile.py
│   ├── quiz.py
│   └── results.py
│
└── utils/
    ├── __init__.py
    └── timer.py