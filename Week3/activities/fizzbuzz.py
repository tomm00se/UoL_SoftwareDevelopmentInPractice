# Exercise: FizzBuzz... 

def fizz_buzz(limit: int):
    """
    This function prints the numbers from 1 to x. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
    """
    for i in range(1, limit+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
            
fizz_buzz(50)