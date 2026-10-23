import re
from utilities import get_file_content

# select_strs(matrix, output_file)
# Given a matrix of strings (list of lists) and a file name, writes to that
# file one line per string that matches the pattern, in the format
# "string;row;column", following the order of the matrix.
# Pattern: 5 to 7 characters, starts with an uppercase vowel (no accents),
# the rest are lowercase letters, and ends with the consonant 'n' or 'l'.
# Note: exam exercise. Strings must be identified using regular expressions.


def select_strs(matrix, output_file):
    pattern = r'^[AEIOU][a-z]{3,5}[nl]$'
    result_words = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            word = matrix[i][j]
            if re.fullmatch(pattern, word):
                word_index = (word, i, j)
                result_words.append(word_index)
    with open(output_file, "w", encoding="utf8") as f_out:
        for word, i, j in result_words:
            f_out.write(f"{word};{i};{j}\n")


if __name__ == '__main__':
    example_matrix = [
        ['Avion', 'sol', 'ESTRELLA', 'Iman'],
        ['python', 'Orden', 'Util', 'Otonel'],
        ['Esfin', 'Abuel', 'Ok', 'Imagen'],
    ]

    select_strs(example_matrix, 'result.txt')

    print('Contents of result.txt:')
    print(get_file_content('result.txt'))
