# Student Grade Management System

A Python command-line program that collects student grades, calculates averages, assigns letter grades, and generates a class report. Built to demonstrate core Python fundamentals: data types, control structures, functions, and error handling.

## Features

- Collects student ID, name, and a configurable number of grades per student
- Calculates each student's average grade
- Assigns a letter grade (A–F) based on average
- Determines pass/fail status against a user-defined passing score
- Generates a final class report summarizing all students
- Validates user input and re-prompts on invalid entries instead of crashing

## Requirements

- Python 3.7 or higher (no external libraries required)

## Setup Instructions

1. Clone this repository:
```bash
   git clone https://github.com/omusula403/student-grade-management-system.git
   cd student-grade-management-system
```

2. Run the program:
```bash
   python grade_manager.py
```
   (Replace `grade_manager.py` with your actual filename if different.)

## How to Use

1. Enter the number of students you want to add.
2. Enter the number of grades to collect per student.
3. Enter a passing score (e.g., 60, 70) — used to determine pass/fail.
4. For each student, enter their ID, name, and grades one at a time.
5. Once all students are entered, the program prints a final class report showing each student's name, average, letter grade, and pass/fail status.

## Example Output
