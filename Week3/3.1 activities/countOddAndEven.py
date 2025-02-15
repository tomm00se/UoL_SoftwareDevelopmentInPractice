# Exercise: Given a list of numbers, cound the number of even and odd numbers in the list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def count_odd_even(numbers:list) -> tuple:
    """
    This function counts the number of even and odd numbers in the list
    """
    odd_count = 0
    even_count = 0
    
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return print("Odd: ", odd_count), print("Even: ", even_count)

count_odd_even(numbers)