import timeit

# The Sample Input
a = {
    'key1': 1,
    'key2': {
            'key3': 1,
            'key4': {
                    'key5': 4
                    }
            }
    }

# A bit more complex nested dict
b = {
    'key0': a,
    'key6': {
            'key7': 1,
            'key8': {
                    'key9': 1,
                    'key10': 1
                    }
            },
    'key11': 0,
    'key12': {
            'key13': 1
            }
    }

# This is the most obvious, cleanest and recursive solution
# to this problem. However, by default python has a recursion
# limit of 1000. If the depth of the dict is more than 1000
# the limit will be trigired causing recursion limit error.
def recursive(data: dict, level: int=1) -> None:
    """
    Prints the depth of every key in a nested dictonary
    """
    for key, value in data.items():
        print(key, level)
        if type(value) is dict:
            recursive(value, level=level+1)

# If one must use map then this is the ugliest solution i could
# come up with. The repeat module from itertools is neeeded in
# this case. However, it's not necessary and can easily be replaced 
# with [level]*len(data.keys())
from itertools import repeat
def recursive_with_map(data: dict, level: int=1) -> None:
    """
    Prints the depth of every key in a nested dictonary
    """
    def print_level(d, level):
        print(d[0], level)
        if type(d[1]) is dict:
            list(map(print_level, d[1].items(), repeat(level+1)))
    list(map(print_level, data.items(), repeat(level)))

# This is a nifty way to solve the problem without trigering the 
# recursion limit while following the same process as the recursive method
def non_recursive(data: dict) -> None:
    """
    Prints the depth of every key in a nested dictonary
    """
    dict_list = [(data, 1)]

    while len(dict_list):
        dict_to_remove = []
        for data, level in dict_list:
            for key, value in data.items():
                print(key, level)
                if type(value) is dict:
                    dict_list.append((value, level+1))
        
            dict_to_remove.append((data, level))

        for value_pair in dict_to_remove:
            dict_list.remove(value_pair)

# This solution is stolen directly from a stackoverflow answer. This 
# solution traverses through the tree like structure formed by a nested 
# dictionary. However, This is the slowest solution as it does multiple 
# passes through the data.
def another_non_recursive(data: dict) -> None:
    """
    Prints the depth of every key in a nested dictonary
    """
    stack = [(data, list(data.keys()))]
    while stack:
        cur, keys = stack.pop()
        while keys:
            k, keys = keys[0], keys[1:]
            print(k, len(stack) + 1)
            value = cur[k]
            if type(value) is dict:
                 stack.append((cur, keys))
                 stack.append((value, list(value.keys())))
                 break

def print_depth(data: dict) -> None:
    """
    Prints the depth of every key in a nested dictonary
    and raises exception if the data is not a dictionary
    """
    if type(data) is not dict:
        raise TypeError("Only dictionaries are allowed.")
    
    recursive(data)

def measure_execution_time(with_print=True):
    """
    This function measures the speed of every solution for this problem
    """
    setup = """
import sys, io
from __main__ import (recursive, recursive_with_map, non_recursive,
                     another_non_recursive, b)
    """
    test_code = """
{}(b)
    """
    test_code_without_print = """
save_stdout = sys.stdout
# sys.stdout = open('trash', 'w')
sys.stdout = io.StringIO()
{}(b)
sys.stdout = save_stdout
    """
    if not with_print:
        test_code = test_code_without_print

    method_list = ['recursive', 'recursive_with_map', 'non_recursive',
                   'another_non_recursive']
    print_string = ''
    for method in method_list:
        # total_time = timeit.timeit(setup=setup, stmt=test_code.format(method), number=10000)
        # print_string = print_string + f'Execution with {method} method took {round(total_time * 1000, 2)} ms \n'

        # This process repeats standard way of measuring execution time of timeit module 10 times. This method 
        # is better because the fastest time represents the best an algorithm can perform when the caches are 
        # loaded and the system isn't busy with other tasks. 
        times = timeit.repeat(setup=setup, stmt=test_code.format(method), repeat=10, number=1000)
        print_string = print_string + f'Execution with {method} method took {round(min(times) * 1000, 2)} ms \n'
    
    print(print_string[:-2])

if __name__ == '__main__':
    print_depth(a)
    # measure_execution_time(False)
