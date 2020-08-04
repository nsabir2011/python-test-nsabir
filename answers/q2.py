import timeit

class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

person_a = Person('User', '1', None)
person_b = Person('User', '2', person_a)

# The sample input
a = {
    'key1': 1,
    'key2': {
            'key3': 1,
            'key4': {
                    'key5': 4,
                    'user': person_b
                    }
            }
    }

class Employee(object):
    def __init__(self, first_name, last_name, designation):
        self.first_name = first_name
        self.last_name = last_name
        self.designation = designation

emp_1 = Employee('bla', 'bla', 'HR')
emp_2 = Employee('bla', 'bla', a)

# A bit more complex nested dict
b = {
    'key1': 1,
    'key2': {
            'key3': 1,
            'key4': {
                    'key5': 4,
                    'key6': a
                    }
            },
    'cls': emp_1,
    'key7': {
            'user': person_b
            }
    }

def class_instance(value):
    # These are the 3 conditions that this problem can be solved with. 
    # However, the 1st one is specific to the sample input calss, it won't work
    # with any other class instance. To make the condition generel to every 
    # class instance the 2nd or the 3rd one should be used.

    # return type(value) is Person:
    # return hasattr(value, '__dict__') and not hasattr(value, '__get__'):
    return hasattr(value, '__dict__') and not callable(value)

def recursive(data: dict, level: int=1, colon: bool=False) -> None:
    """
    Prints the depth of every key in a nested dictonary or class instance
    """
    for key, value in data.items():

        if colon or class_instance(value):
            print(f'{key}: {level}')
        else:
            print(key, level)

        if type(value) is dict:
            recursive(value, level=level+1)
        elif class_instance(value):
            recursive(value.__dict__, level=level+1, colon=True)

def print_depth(data: dict) -> None:
    """
    Prints the depth of every key in a nested dictonary
    and raises exception if the data is not a dictionary
    """
    if type(data) is not dict and not class_instance(data):
        raise TypeError("Only dictionaries or class instances are allowed.")
    
    if class_instance(data):
        data = data.__dict__
        recursive(data, level=1, colon=True)
    else:
        recursive(data, level=1, colon=False)

if __name__ == '__main__':
    print_depth(a)