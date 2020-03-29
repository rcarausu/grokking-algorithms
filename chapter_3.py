"""
Recursion
- When a function calls itself
Base case -> when it stops
Recursive case -> when it calls itself
"""


# Exercise 3.1
# From that stack, we can say that we are calling a greet function with the Maggie variable,
# which it's calling the greet2 function with the same variable name.

# Exercise 3.2
# A recursive function that runs forever will fill the stack and thus the memory.
# The computer will crash.

def factorial(x: int):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)


if __name__ == '__main__':
    print(factorial(5))
