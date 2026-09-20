# Hardest Exam

Python function that finds the hardest exam of a subject, meaning the one with the lowest average grade, from a nested academic data structure (subjects, students, exams).

`get_hardest_exam(data, subject_code)` returns a tuple `(description, date, average_grade)`. It returns `"NOASIG"` if the subject does not exist and `"NOEXAM"` if it has no exams (fixed return values from the assignment).

This was an exam exercise. The data structure format was given in the assignment, and `sample_data.py` only contains test data.

## Run

    python hardest_exam.py
