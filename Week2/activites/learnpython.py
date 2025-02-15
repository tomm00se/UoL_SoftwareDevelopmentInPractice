# Example 1
number = 1 + 2 * 3 / 4.0
print(number) # 2.5

# Example 2
remainder = 11 % 3 # % is the modulo operator
print(remainder) # 2

# Example 3
squared = 7 ** 2 # ** is the exponentiation operator
cubed = 2 ** 3
print(squared) # 49
print(cubed) # 8

# Example 4
helloworld = "hello" + " " + "world" # + is the string concatenation operator (as well as integer addition)
print(helloworld)

# Example 5
lotsofhellos = "hello" * 10 # * is the string repetition operator
print(lotsofhellos) # hellohellohellohellohellohellohellohellohellohello

# Example 6
even_numbers = [2,4,6,8] # [] is the list operator
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers # + is the list concatenation operator
all_numbers_inverse = even_numbers + odd_numbers
print(all_numbers) # [1, 3, 5, 7, 2, 4, 6, 8]
print(all_numbers_inverse) # [2, 4, 6, 8, 1, 3, 5, 7]

# Example 7
print([1,2,3] * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3] * is the list repetition operator

# Exercise 1

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10 # [x] * 10 creates a list with 10 elements, all of which are x
y_list = [y] * 10 # [y] * 10 creates a list with 10 elements, all of which are y
big_list = x_list + y_list # x_list + y_list concatenates the two lists into one list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")