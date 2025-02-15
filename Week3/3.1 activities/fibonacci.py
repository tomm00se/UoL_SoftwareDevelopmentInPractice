# Exercise: Create a function that generates the Fibonacci sequence up to a certain number.

def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a certain number.
    """
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b # This is a tuple unpacking. It is a way to assign multiple variables at once. a becomes b and b becomes a+b
    print()
    
fibonacci(50)
    