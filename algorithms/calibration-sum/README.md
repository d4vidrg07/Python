# Calibration sum

Given a list of strings, combine the first and last digit of each string
into a two-digit number and return the sum of all of them.

- A string with a single digit uses it as both first and last digit.
- A string with no digits adds nothing.

## Approach

Two indices scan each string, one from the left and one from the right,
until each finds a digit. The two digits are joined, converted to `int`
and added to the total. Strings without digits are skipped.

## Example

Input:

```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```

Output:

```
142
```

Because `12 + 38 + 15 + 77 = 142`.

## Edge cases

- Empty string or string without digits: adds nothing.
- Single digit: used as both first and last digit (e.g. `treb7uchet` -> `77`).
- Empty list: returns `0`.

## Complexity

- Time: O(n) per string, where n is its length (each index moves at most n positions).
- Extra space: O(1).

## Running the tests

```
pip install pytest
pytest
```
