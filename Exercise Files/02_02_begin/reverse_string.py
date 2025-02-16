"""
Python Data Structures - A Game-Based Approach
Stack challenge
Robin Andrews - https://compucademy.net/
"""

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# Your solution here.
def reverse_string(words):
    reversed_string = ""
    s = stack.Stack()
    
    for char in words:
        s.push(char)
    
    while not s.is_empty():
        reversed_string += s.pop()
    
    return reversed_string

print(reverse_string(string))
