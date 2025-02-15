# Exercise: Create a program that prints the following pattern:
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

def star_art(n):
    """
    This function prints the star art pattern
    """
    for i in range(n):
        for j in range(i):
            print("*", end=" ")
        print("")
    
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print("")
        
print(star_art(5))