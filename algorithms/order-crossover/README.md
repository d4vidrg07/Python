# S1a - Order Crossover

Implementation of the Order Crossover operator used in genetic algorithms. Given two parent lists with the same elements in different order and two cut points, it builds a child list:

1. The segment `parent1[lower_bound:upper_bound]` is copied into the child, in the same positions.
2. The rest of the child is filled with the elements of `parent2`, read circularly from position `upper_bound`, skipping elements already in the child.

`order_crossover(parent1, parent2, lower_bound, upper_bound)` returns the child list.

Example:

    parent1     = [8, 11, 3, 5, 6, 4, 2, 12, 1, 9, 7, 10]
    parent2     = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    lower_bound = 6
    upper_bound = 9
    child       = [4, 5, 6, 7, 8, 9, 2, 12, 1, 10, 11, 3]

Only `solve.py` is my own code. `main.py` and `utils.py` come from the course template (they handle input and output), and `test1.txt` is my own sample input.

## Run

    python main.py < test1.txt
