# Algorithms & Programming: Highlights

A selection of exercises from the **Algorithms and Programming** course (ULPGC) that I consider representative of my work. The full course repository is [Algorithms-and-Programming-](https://github.com/d4vidrg07/Algorithms-and-Programming-). Each folder has its own README with the problem, the approach, the complexity and how to run it.

## Python idioms and string/list processing

| Exercise | What it shows |
|---|---|
| [Order crossover](order-crossover) | Genetic-algorithm operator: slicing, circular traversal and membership checks on lists. |
| [Calibration sum](calibration-sum) | String parsing from both ends, edge cases and unit tests with `pytest`. |
| [`select_strs`](../exams/select-strs-regex) | Regular expressions and text file output (exam exercise). |
| [`get_hardest_exam`](../exams/hardest-exam) | Nested dictionaries and aggregation (exam exercise). |

## How to run

Each exercise folder contains its own instructions. In general:

```
python main.py < test1.txt      # exercises with a main.py and a sample input
pytest                          # exercises with unit tests
```

More highlights (graph algorithms, backtracking and dynamic programming) will be added here as I complete them.
