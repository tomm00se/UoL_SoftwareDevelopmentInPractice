# Exercise: Create timing tests for iterative_towers_of_hanoi
import timeit
from towersOfHanoi import iterative_towers_of_hanoi

# Define a wrapper function to call iterative_towers_of_hanoi with a specific number of disks
def test_iterative_towers_of_hanoi(n):
    iterative_towers_of_hanoi(n)

# Measure the execution time for different numbers of disks
for n in range(1, 6): # Test for 1 to 5 disks
    time_taken = timeit.timeit(lambda: test_iterative_towers_of_hanoi(n), number=1)
    print(f"Time taken for {n} disks: {time_taken:.6f} seconds")
