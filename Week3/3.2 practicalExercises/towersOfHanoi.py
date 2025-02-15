#Exercise: Create an imperitive solution to the towers of hanoi problem.

def iterative_towers_of_hanoi(n:int):
    """
    This function solves the towers of hanoi problem using an iterative solution
    param: n: The number of disks
    """
    #Create a stack for each rod
    source = list(range(n,0,-1)) # The source rod has the disks in descending order from n to 1.
    auxiliary = [] # The auxiliary rod is empty
    target = [] # The target rod is empty
    
    # Determine the total number of moves based on the number of disks
    total_moves = 2**n - 1
    
    # If the number of disks is even, swap the auxiliary and target rods
    if n % 2 == 0:
        auxiliary, target = target, auxiliary
    
    # Print the initial state of the rods
    print(f"Initial State: S:{source} A: {auxiliary} T: {target}")
    
    # Iterate through the total number of moves
    for move in range(1, total_moves + 1):
        if move % 3 == 1:
            move_disk(source, target, "S", "T")
        elif move % 3 == 2:
            move_disk(source, auxiliary, "S", "A")
        elif move % 3 == 0:
            move_disk(auxiliary, target, "A", "T")
    
    # Print final state of the rods        
    print(f"Final state: Source: {source}, Auxiliary: {auxiliary}, Target: {target}")           
            
def move_disk(from_rod, to_rod, from_name, to_name):
    if not from_rod: # If the from rod is empty, move the disk from the to rod to the from rod
        from_rod.append(to_rod.pop())
        print(f"Move disk from {to_name} to {from_name}")
    elif not to_rod: # If the to rod is empty, move the disk from the from rod to the to rod
        to_rod.append(from_rod.pop())
        print(f"Move disk from {from_name} to {to_name}")
    elif from_rod[-1] > to_rod[-1]: # If the disk on the from rod is larger than the disk on the to rod, move the disk from the to rod to the from rod
        from_rod.append(to_rod.pop())
        print(f"Move disk from {to_name} to {from_name}")
    else: # If the disk on the from rod is smaller than the disk on the to rod, move the disk from the from rod to the to rod
        to_rod.append(from_rod.pop())
        print(f"Move disk from {from_name} to {to_name}")
        
iterative_towers_of_hanoi(3)