from sample_data import data

    """Return (description, date, average) of the exam with the lowest
    average grade for the given subject, or "NOASIG" / "NOEXAM"."""


def get_hardest_exam(data, subject_code):

    if subject_code not in data[0]:
        return "NOASIG"

    subject_exam_codes = []

    for exam_code in data[2]:
        if data[2][exam_code][1] == subject_code:
            subject_exam_codes.append(exam_code)

    if len(subject_exam_codes) == 0:
        return "NOEXAM"

    hardest_exam_code = None
    lowest_average = float("inf")

    for exam_code in subject_exam_codes:
        grade_sum = 0.0
        num_students = 0
        for grade in data[2][exam_code][3].values():
            grade_sum += grade
            num_students += 1

        exam_average = grade_sum / num_students

        if exam_average < lowest_average:
            hardest_exam_code = exam_code
            lowest_average = exam_average

    description = data[2][hardest_exam_code][0]
    date = data[2][hardest_exam_code][2]

    return (description, date, lowest_average)


if __name__ == "__main__":
    # Existing subject with exams
    print(get_hardest_exam(data, "10002"))

    # Non-existent subject
    print(get_hardest_exam(data, "99999"))

    # Existing subject without exams
    print(get_hardest_exam(data, "30001"))
