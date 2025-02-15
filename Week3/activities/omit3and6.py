#Exercise: Create a function that lists numbers from 1 - 6 but omits 3 and 6.

def omit_3_and_6():
    """
    This function lists numbers from 1 - 6 but omits 3 and 6.
    """
    for i in range(1, 7):
        if i == 3 or i == 6: 
            continue # Skip 3 and 6 by continuing to the next iteration, skipping the print statement.
        print(i)
        
omit_3_and_6()