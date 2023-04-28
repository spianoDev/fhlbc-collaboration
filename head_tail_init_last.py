# https://www.codewars.com/kata/54592a5052756d5c5d0009c3
# Level 7 kyu

# Your job is to implement 4 functions that return values in this exact structure.
# | HEAD | <----------- TAIL ------------> |
# [  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
# | <----------- INIT ------------> | LAST |

# head [x] = x
# tail [x] = []
# init [x] = []
# last [x] = x


# Solution.
def head(init: list):
    """Returns first element from given list."""
    return init[0]


def tail(array: list) -> list:
    """Returns all elements from given list other than first element."""
    tail: list = array[1:]
    return tail


def init(array: list) -> list:
    """Returns all elements from given list other than the last element."""
    init: list = array[:-1]
    return init


def last(tail: list):
    """Returns last element from given list."""
    return tail[-1]


# Tests.
# print(head([1,2,3,4,5])) # -> 1
# print(tail([1,2,3,4,5])) # -> [2,3,4,5]
# print(init([1,2,3,4,5])) # -> [1,2,3,4]
# print(last([1,2,3,4,5])) # -> 5