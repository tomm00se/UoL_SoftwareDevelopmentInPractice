# Exercise: Write a program to find numbers divisable by 7 and multiple of 5 between 1500 and 2700

def find_numbers(lower_bound:int, upper_bound:int) -> list:
    """
    This function finds numbers that are divisible by 7 and multiples of 5
    between 1500 and 2700
    """
    result = []
    
    for n in range(lower_bound, upper_bound):
        if n % 7 == 0 and n % 5 == 0:
            result.append(n)
    return result

print(find_numbers(1500, 2700))