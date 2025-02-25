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

