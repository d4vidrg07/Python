def order_crossover(parent1, parent2, lower_bound, upper_bound):
    child = [None] * len(parent1)

    child[lower_bound:upper_bound] = parent1[lower_bound:upper_bound]

    child_pos = upper_bound
    parent2_pos = upper_bound

    while None in child:

        if parent2_pos == len(parent2):
            parent2_pos = 0
        if child_pos == len(parent2):
            child_pos = 0

        if child[child_pos] != None:
            child_pos += 1

        elif parent2[parent2_pos] not in child:
            child[child_pos] = parent2[parent2_pos]
            child_pos += 1

        parent2_pos += 1

    return child
