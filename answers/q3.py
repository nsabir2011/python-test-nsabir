import timeit
from itertools import combinations_with_replacement

# The Samle Node Class from the question
class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

# The Sample Tree Structure
node_1 = Node(1, None)
node_2 = Node(2, node_1)
node_3 = Node(3, node_1)
node_4 = Node(4, node_2)
node_5 = Node(5, node_2)
node_6 = Node(6, node_3)
node_7 = Node(7, node_3)
node_8 = Node(8, node_4)
node_9 = Node(9, node_4)
node_10 = Node(10, node_5)     # The question does not have this node

# This solution traverses from the input node to the root and records each nodes path to 
# find the LCA.
# The worst case time complexity or runtime is O(n) where n is the number of times each leaf node
# traverse and the best case time complexity or runtime is Ω(1).
# The worst case space complexity or memory footprint is O(n) where n is the number of times both 
# leaf nodes traverses to reach the root.
def recursive(node1: Node, node2: Node, node1_values: list, node2_values: list) -> Node:
    """
    Returns the lowest common ancestor of a binary tree
    """
    if node1.value is node2.value:
        return node1

    node1_values.append(node1.value)
    node2_values.append(node2.value)

    if node1.parent is not None:
        node1 = node1.parent
        if node1.value in node2_values:
            return node1
        node1_values.append(node1.value)

    if node2.parent is not None:
        node2 = node2.parent
        if node2.value in node1_values:
            return node2
        node2_values.append(node2.value)

    return recursive(node1, node2, node1_values, node2_values)

# This solution traverses from the input node to the root and records each node's path to 
# find the LCA.
# The worst case time complexity or runtime is O(n) and the best case time complexity or runtime is Ω(1).
# The space complexity or memory footprint is O(n) if the recursive stack space is ignored.
def another_recursive(node1: Node, node2: Node, node1_values: list, node2_values: list) -> Node:
    """
    Returns the lowest common ancestor of a binary tree
    """
    if node1.parent is None:
        return node1

    if node2.parent is None:
        return node2

    if node1.value is node2.value:
        return node1

    if node1.parent.value is node2.parent.value:
        return node1.parent

    node1_values.append(node1.value)
    node2_values.append(node2.value)

    if node1.parent.value in node2_values:
        return node1.parent

    if node2.parent.value in node1_values:
        return node2.parent

    loop_node1 = node1
    while True:
        if loop_node1.parent is not None:
            if loop_node1.value is node2.value:
                return node2
            loop_node1 = loop_node1.parent
        else:
            break

    loop_node2 = node2
    while True:
        if loop_node2.parent is not None:
            if loop_node2.value is node1.value:
                return node1
            loop_node2 = loop_node2.parent
        else:
            break

    return another_recursive(node1.parent, node2.parent, node1_values, node2_values)

# This solution traverses from the input node to the root and records each nodes path to 
# find the LCA.
# The worst case time complexity or runtime is O(n) where n is the number of times each leaf node
# traverse and the best case time complexity or runtime is Ω(1).
# The worst case space complexity or memory footprint is O(n) where n is the number of times both 
# leaf nodes traverses to reach the root.
def non_recursive(node1: Node, node2: Node) -> Node:
    """
    Returns the lowest common ancestor of a binary tree
    """
    if node1.value is node2.value:
        return node1

    if node1.parent is None:
        return node1

    if node2.parent is None:
        return node2

    if node1.parent.value is node2.parent.value:
        return node1.parent

    node1_values = [node1.value]
    node2_values = [node2.value]

    while True:
        if node1.parent is not None:
            node1 = node1.parent
            if node1.value in node2_values:
                return node1
            node1_values.append(node1.value)

        if node2.parent is not None:
            node2 = node2.parent
            if node2.value in node1_values:
                return node2
            node2_values.append(node2.value)

def lca(node1: Node, node2: Node) -> Node:
    """
    Returns the lowest common ancestor of a binary tree as well as 
    prints the solution and execution time
    """
    if type(node1) is not Node or type(node2) is not Node:
        raise TypeError('Only Node instances are allowed')
    
    # solution = recursive(node1, node2, [], [])
    # solution = another_recursive(node1, node2, [], [])
    solution = non_recursive(node1, node2)
    print(solution.value)
    return solution

def find_lca_for_all_combinations(method=non_recursive):
    """
    finds the lowest common ancestor of the sample binary tree 
    for all possible combinations
    """
    for pair in combinations_with_replacement([node_1, node_2, node_3, node_4, 
                node_5, node_6, node_7, node_8, node_9, node_10], r=2):
        if method is non_recursive:
            solution = method(*pair)
        else:
            solution = method(*pair, [], [])
        print(f'LCA for node {pair[0].value} and {pair[1].value} is {solution.value}')

def measure_execution_time(with_print=True):
    """
    This function measures the speed of every solution for this problem
    """
    setup = """
import sys, io
from itertools import permutations
from __main__ import (recursive, another_recursive, non_recursive,
                     find_lca_for_all_combinations)
    """
    test_code = """
find_lca_for_all_combinations({})
    """
    test_code_without_print = """
save_stdout = sys.stdout
# sys.stdout = open('trash', 'w')
sys.stdout = io.StringIO()
find_lca_for_all_combinations({})
sys.stdout = save_stdout
    """
    if not with_print:
        test_code = test_code_without_print

    method_list = ['recursive', 'another_recursive', 'non_recursive']
    print_string = ''
    for method in method_list:
        # total_time = timeit.timeit(setup=setup, stmt=test_code.format(method), number=10000)
        # print_string = print_string + f'Execution with {method} method took {round(total_time * 1000, 2)} ms \n'

        # This process repeats the standard way of measuring execution time of timeit module 10 times. This method 
        # is better because the fastest time represents the best an algorithm can perform when the caches are 
        # loaded and the system isn't busy with other tasks.
        times = timeit.repeat(setup=setup, stmt=test_code.format(method), repeat=10, number=1000)
        print_string = print_string + f'Execution with {method} method took {round(min(times) * 1000, 2)} ms \n'

    print(print_string[:-2])

if __name__ == "__main__":
    # find_lca_for_all_combinations()
    # measure_execution_time(False)
    lca(node_6, node_7)
    lca(node_3, node_7)