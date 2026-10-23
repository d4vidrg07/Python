# Select Strs

Python function that scans a matrix of strings (list of lists) and writes to a text file the strings that match a pattern, together with their row and column indexes. The matching is done with regular expressions.

A string matches if it has 5 to 7 characters, starts with an uppercase vowel (no accents), continues with lowercase letters only, and ends with the consonant `n` or `l`.

`select_strs(matrix, output_file)` writes one line per match in the format `string;row;column`, in matrix order. For the example matrix in the script, the output is:

    Avion;0;0
    Orden;1;1
    Otonel;1;3
    Esfin;2;0
    Abuel;2;1
    Imagen;2;3

This was an exam exercise. `utilities.py` only contains a helper to read a file, not part of the solution.

## Run

    python select_strs.py
