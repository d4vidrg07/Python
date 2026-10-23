data = (
    # Subjects: code -> (name, semester, credits, {enrolled DNIs}, {exam codes})
    {
        "10001": ("Linear Algebra", 1, 6, {"11111111A", "22222222B"}, {"EXA01"}),
        "10002": ("Calculus", 1, 6, {"11111111A", "33333333C"}, {"EXC01", "EXC02"}),
        "20001": ("Data Structures", 3, 4.5, {"22222222B", "33333333C"}, {"EXE01"}),
        "30001": ("Software Engineering", 3, 4.5, {"22222222B", "33333333C"}, set()),
    },
    # Students: DNI -> (full name, {subject codes}, {taken exam codes})
    {
        "11111111A": ("Juan Pérez", {"10001", "10002"}, {"EXA01", "EXC01"}),
        "22222222B": ("Ana López", {"10001", "20001"}, {"EXA01", "EXE01"}),
        "33333333C": ("Luis García", {"10002", "20001"}, {"EXC02"}),
    },
    # Exams: code -> (description, subject code, date dd/mm/yyyy, {DNI: grade})
    {
        "EXA01": ("Linear Algebra midterm", "10001", "15/10/2025",
                  {"11111111A": 7.5, "22222222B": 8.0}),
        "EXC01": ("Calculus midterm 1", "10002", "20/10/2025",
                  {"11111111A": 6.2}),
        "EXC02": ("Calculus midterm 2", "10002", "10/12/2025",
                  {"33333333C": 9.1}),
        "EXE01": ("Data Structures final exam", "20001", "18/12/2025",
                  {"22222222B": 7.8}),
    },
)
