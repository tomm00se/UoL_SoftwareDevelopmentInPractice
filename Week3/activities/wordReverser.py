# Exercise: Take a string as input and return the reverse of the string

def reverse_string():
    """
    This function takes a string as input and returns the reverse of the string
    """
    user_input = input("Enter a string: ")
    return print("That word reversed is: ", user_input[::-1])

reverse_string()