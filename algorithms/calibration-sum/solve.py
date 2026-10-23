def solve(input_list):
    """
    Computes the sum of the calibration values of a list of strings.

    Parameters:
        input_list: list of strings. Each string may contain letters,
        digits or other characters.

    Expected behavior:
        1. Process each string in input_list.
        2. Find the first digit and the last digit of each string.
        3. Join those two digits into a two-digit number.
        4. If a string contains a single digit, use it as both the first
           and the last digit.
        5. If a string contains no digits, add nothing for that string.
        6. Return the total sum of all the numbers obtained.

    Restrictions:
        - Do not read keyboard input inside this function.
        - Do not print results inside this function.
        - Return an integer.
    """

    total = 0

    for line in input_list:

        digits = []

        start_idx = 0
        end_idx = len(line) - 1

        while start_idx < len(line) and not line[start_idx].isdigit():
            start_idx += 1

        if start_idx >= len(line):
            continue

        digits.append(str(line[start_idx]))

        while end_idx >= 0 and not line[end_idx].isdigit():
            end_idx -= 1

        digits.append(str(line[end_idx]))

        joined_digits = "".join(digits)

        total += int(joined_digits)

    return total
