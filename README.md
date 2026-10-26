# Python Mini Projects 🐍

A collection of beginner-friendly Python projects built to practice programming fundamentals, problem-solving, file handling, automation, and modular application design.

The repository contains small projects that gradually explore different concepts through practical implementations.

---

## 📂 Projects

| Project | Description | Concepts |
|---|---|---|
| 🔐 **Password Generator** | Generates secure random passwords based on user requirements. | Randomization, Strings, Functions |
| 🎲 **Dice Roller** | Simulates rolling one or more dice. | Randomization, Loops, User Input |
| 💰 **Expense Tracker** | Tracks and manages personal expenses through a simple Python interface. | File Handling, Data Structures, Functions |
| 💬 **Quote Extractor** | Extracts quotes from web pages and displays them. | Web Scraping, Requests, HTML Parsing |
| 🔢 **Number Guessing Game** | A game where the user attempts to guess a randomly generated number. | Randomization, Loops, Conditional Logic |
| 🧠 **Quiz Application** | A modular console-based quiz system with authentication, randomized questions, categories, timer, and results. | JSON, Modules, Randomization, Threading, Authentication |

---

# 🧠 Quiz Application

A modular terminal-based quiz application designed to simulate a simple online quiz system directly from the command line.

### Features

- 👤 User registration
- 🔑 User login
- 📋 Profile management
- ✏️ Update profile
- 🧠 Multiple quiz categories
- 🎲 Random question selection
- 🔀 Randomized answer options
- ⏱️ 30-second timer per question
- ⚠️ Automatic timeout
- 📊 Score calculation
- ✅ Pass/Fail evaluation
- 📈 Persistent quiz results
- 📚 JSON-based question database

### Quiz Categories

The application currently provides:

1. DSA
2. DBMS
3. Python
4. System Design

### Quiz Flow

```text
                    Quiz Application
                           │
            ┌──────────────┴──────────────┐
            │                             │
       Registration                     Login
                                          │
                                   ┌──────┴──────┐
                                   │             │
                                Profile      Update Profile
                                   │
                                   └──────┬──────┘
                                          │
                                    Attempt Quiz
                                          │
                   ┌──────────────┬───────┼──────────────┐
                   │              │       │              │
                  DSA           DBMS    Python     System Design
                   │              │       │              │
                   └──────────────┴───────┴──────────────┘
                                          │
                                   Random Questions
                                          │
                                    30 Sec / Question
                                          │
                                        Result
                                          │
                                       Logout
```

---

## 📁 Quiz Application Structure

```text
Quiz_Application/
│
├── main.py
│
├── data/
│   └── questions.json
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
```

### Module Responsibilities

**`main.py`**

Entry point of the application. Handles the main menu and routes users to registration, login, or exit.

**`modules/auth.py`**

Handles user registration, authentication, dashboard navigation, and logout.

**`modules/database.py`**

Provides reusable functions for reading and writing JSON data.

**`modules/profile.py`**

Handles profile display and profile updates.

**`modules/quiz.py`**

Contains quiz logic, question randomization, option randomization, answer validation, scoring, and result generation.

**`modules/results.py`**

Retrieves and displays previous quiz attempts for the logged-in user.

**`utils/timer.py`**

Provides the 30-second question timer.

**`data/questions.json`**

Contains the question bank for all supported quiz categories.

---

# ⚙️ Technologies Used

- **Python**
- **JSON**
- **Python Standard Library**
- `random`
- `threading`
- File handling
- Modular programming

No external Python packages are required for the current version.

---

# 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Arpit170506/Python_mini_projects.git
```

### 2. Navigate to the project

```bash
cd Python_mini_projects/Quiz_Application
```

### 3. Run the application

```bash
python main.py
```

---

# 🎯 Purpose

This repository is primarily a learning project.

The projects are built to practice:

- Python fundamentals
- Functions
- Loops
- Conditional statements
- Data structures
- File handling
- JSON data storage
- Randomization
- Modular programming
- Basic application architecture
- Problem-solving

The goal is to gradually move from simple Python scripts toward more structured and modular applications.

---

# 🔮 Future Improvements

Possible improvements for the Quiz Application include:

- Password hashing
- SQLite database
- Larger question bank
- Difficulty levels
- Question categories
- Leaderboard
- User statistics
- Quiz history
- Admin question management
- Improved terminal timer
- Better input validation
- Automated tests
- GUI/Web version

---

## 📌 Current Status

| Project | Status |
|---|---|
| Password Generator | ✅ Complete |
| Dice Roller | ✅ Complete |
| Number Guessing Game | ✅ Complete |
| Quote Extractor | ✅ Complete |
| Expense Tracker | ✅ Complete |
| Quiz Application | 🚧 MVP |

---

## 👨‍💻 Author

**Arpit Mishra**

Computer Science Engineering student specializing in Artificial Intelligence & Machine Learning.

- GitHub: [Arpit170506](https://github.com/Arpit170506)
- LinkedIn: [Arpit Mishra](https://www.linkedin.com/in/arpit-mishra-283a47307)

---

## ⭐ Feedback & Contributions

This repository is primarily maintained as a personal learning and project portfolio.

Suggestions, improvements, and constructive feedback are welcome.