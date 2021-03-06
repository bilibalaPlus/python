"""Some exercises involving lists.

`creating lists
==============
a='A'
b='B'
c='C'
x = list()
add a, b, c into x
print the length of x

selecting from lists
====================
Given the list
x = ['A', 'B', 'C']
return the first item
return the last item
return the x reversed using indexing

selecting first items
======================= 
Given the following:
x = [('A','x'), ('B','y'), ('C','z')]
return ['A','B','C']

add 5 to values
=================
Given the following:
x = [1, 10, 20]
return a list with 5 added to the numbers i.e. [6, 15, 25]

divisible by 5
==================
Given the following:
x = [1, 10,  15, 3, 12, 15, 25, 50]
return a list with only numbers divisible by 5 (% modulo operator)

merge_lists
===================
given the lists:
x = ['A', 'B', 'C']
y = ['x', 'y', 'z']
create the following list:
[('A','x'), ('B','y'), ('C','z')]

transpose()
===========
Create a function that takes a list of lists and returns the transpose. So given:
[
    [1, 2, 3],
    ['A', 'B', 'C'],
]

We would expect:
[
    [1, 'A'],
    [2, 'B'],
    [3, 'C'],
]

In the case of uneven length lists choose then truncate to the shortest, so given:
[
    [1, 2, 3],
    ['A', 'B'],
]

We would expect:
[
    [1, 'A'],
    [2, 'B'],
]

Hint: There is a builtin function that can help you.

peak_to_peak()
==============
Create a function that returns the peak-to-peak value of the values in a list.

Hint: There are a couple of builtin functions that can help you.

Challenges: What to do when the list is empty?
If the list contains non-numeric values?

list rotation
=============
Rotate a list by taking the value from one end a putting it on the other end.
Create two functions rotate_left() and rotate_right() that modify a list in
place as follows, given the list ['A', 'B', 'C']:

rotate_left() changes it to ['B', 'C', 'A']
rotate_right() changes it to ['C', 'A', 'B']
"""
"""import pytest"""

def create_list():
    """Create a list."""
    a ='A'
    b ='B'
    c ='C'
    x=list()
    x.append(a)
    x.append(b)
    x.append(c)
    print(len(x))

def select_first_item():
    """Return first item."""
    x = ['A', 'B', 'C']
    return x[0]

def select_last_item():
    """Return last item."""
    x = ['A', 'B', 'C']
    return x[-1]

def select_reversed():
    """Return list reversed."""
    x = ['A', 'B', 'C']
    print(x[::-1])

def select_first_items():
    """Select first item on each list."""
    x = [('A','x'), ('B','y'), ('C','z')]
    print(list(i[0] for i in x))

def add_5_to_values():
    """Return the list with 5 added to each value."""
    x = [1, 10, 20]
    print(list(i+5 for i in x))

def get_divisble_by_5():
    """Return elements that are divisble by 5."""
    x = [1, 10,  15, 3, 12, 15, 25, 50]
    print(list(i for i in x if(i%5==0)))

def merge_lists():
    """Returns pairs from each list."""
    x = ['A', 'B', 'C']
    y = ['x', 'y', 'z']
    print(list(zip(x,y)))

def transpose(list_of_lists):
    """Transpose a list of lists."""
    return(list(list(v) for v in zip(*list_of_lists)))

def peak_to_peak(alist):
    """Return the peak to peak value of a list."""
    pass

def rotate_left(alist):
    """Rotates a list to the left so that the first item appears at the end."""
    pass

def rotate_right(alist):
    """Rotates a list to the right so that the last item appears at the beginning."""
    pass

#=================== Tests ========================
def test_create_list():
    assert create_list() == ['A', 'B', 'C']

def test_select_first_item():
    assert select_first_item() == 'A'

def test_select_last_item():
    assert select_last_item() == 'C'
    
def test_select_reversed():
    assert select_reversed() == ['C', 'B', 'A']
    
def test_select_first_items():
    assert select_first_items() == ['A','B','C']
    
def test_add_5_to_values():
    assert add_5_to_values() == [6, 15, 25]
    
def test_get_divisble_by_5():
    assert get_divisble_by_5() == [10, 15, 15, 25, 50]
    
def test_merge_lists():
    assert merge_lists() == [('A', 'x'), ('B', 'y'), ('C', 'z')]

def test_transpose():
    data = [
        [1, 2, 3],
        ['A', 'B', 'C'],
    ]
    expected = [
        [1, 'A'],
        [2, 'B'],
        [3, 'C'],
    ]
    assert transpose(data) == expected

def test_transpose_non_equal_length():
    data = [
        [1, 2, 3],
        ['A', 'B'],
    ]
    expected = [
        [1, 'A'],
        [2, 'B'],
    ]
    assert transpose(data) == expected

def test_peak_to_peak():
    assert peak_to_peak([1, 8]) == 7
    assert peak_to_peak([-1, -8]) == 7
    assert peak_to_peak([9, -8]) == 17

def test_rotate_left():
    l = ['A', 'B', 'C']
    rotate_left(l)
    assert l ==  ['B', 'C', 'A']

def test_rotate_right():
    l = ['A', 'B', 'C']
    rotate_right(l)
    assert l == ['C', 'A', 'B']

def test_rotate_left_empty():
    l = []
    rotate_left(l)
    assert l == []

def test_rotate_right_empty():
    l = []
    rotate_right(l)
    assert l == []

def main():
    create_list()
    print(select_first_item())
    print(select_last_item())
    select_reversed()
    select_first_items()
    add_5_to_values()
    get_divisble_by_5()
    merge_lists()
    test_transpose()
    test_transpose_non_equal_length()

    return """pytest.main(__file__)"""

if __name__ == '__main__':
    main()
