"""
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
"""

# Best Practice
def maps(a):
    return [2 * x for x in a]

# Me
def maps(a):
    doubled_ints = []
    for num in a:
        num += num
        doubled_ints.append(num)
    return doubled_ints

