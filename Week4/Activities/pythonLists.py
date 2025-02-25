# 1 - Reverse a list in Python
list1 = [100, 200, 300, 400, 500]
result = list1.reverse()
print(result)

# 2 - Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = [i + j for i, j in zip(list1, list2)]
print(result)

# 3 - Turn every item of a list into its square
numbers = [1, 2, 3, 4, 5, 6, 7]
squaredNumbers = []
for i in numbers:
    squaredNumbers.append(i * i)

print(squaredNumbers)

# 4 - Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
result = [x + y for x in list1 for y in list2]
print(result)

# 5 - Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)
    
# 6 - Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

result = list(filter(None, list1))
print(result)

# 7 - Add new item to list after a specified item
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# output: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#8 - Extend nested list by adding the sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

# understand indexing
# list1[2] = ['c', ['d', 'e', ['f', 'g'], 'k'], 'l']
# list1[2][1] = ['d', 'e', ['f', 'g'], 'k']
# list1[2][1][2] = ['f', 'g']

list1[2][1][2].extend(sub_list)
print(list1)

# 9 - Replace list’s item with new value if found
list1 = [5, 10, 15, 20, 25, 50, 20]
# outcome: [5, 10, 15, 200, 25, 50, 20]

index = list1.index(20)

list1[index] = 200
print(list1)

# 10 - Remove all occurrences of a specific item from a list.
list1 = [5, 20, 15, 20, 25, 50, 20]
# outcome: [5, 15, 25, 50]

def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]

result = remove_value(list1, 20)
print(result)