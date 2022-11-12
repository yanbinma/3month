from collections import namedtuple

Pointer = namedtuple("Pointer", ['name', 'value'])
def print_pointers(s, *pointers):
    '''
        print string with multiple pointers for ease debugging
        pointers must be sorted and within range; otherwise print error message
        ref: https://realpython.com/python-f-strings/
        ref: https://docs.python.org/3.6/library/collections.html?highlight=namedtuple#collections.namedtuple
    '''
    print(s)
    for p in pointers: 
        print('*'*p.value, end="")
        print(f"^{p.name}={p.value}")


