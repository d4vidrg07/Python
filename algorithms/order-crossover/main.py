from utils import open_test_file, close_test_file, get_line
from solve import *

TEST_FILE = None
# TEST_FILE = "test1.txt"

input_source = open_test_file(TEST_FILE)

string1 = get_line(input_source)
parent1 = [int(k) for k in string1.split(',')]

string2 = get_line(input_source)
parent2 = [int(k) for k in string2.split(',')]

lower_bound = int(get_line(input_source))
upper_bound = int(get_line(input_source))

solution = order_crossover(parent1, parent2, lower_bound, upper_bound)

print(solution)

close_test_file(TEST_FILE, input_source)

