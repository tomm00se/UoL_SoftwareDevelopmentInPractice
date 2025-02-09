import re
# Example 1 : Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

# Example 2 : Check if the string contains "ai" followed by 0 or more "x" characters:
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x) # Output: ['ai', 'ai'] from rain and Spain

# Example 3 : Check if the string contains "Portugal":
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x) # Output: [] since Portugal is not in the string

# Example 4 : Check if the string contains "ai" followed by 1 or more "x" characters:

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
# Output: The first white-space character is located in position: 3

# Example 5 : Check if the string contains a specific string value (Portugal):
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x) # Output: None - since Portugal is not in the string

# Example 6 : Split the string at every white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) # Output: ['The', 'rain', 'in', 'Spain']

# Example 7 : Split the string at the first white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x) # Output: ['The', 'rain in Spain']

# Example 8 : Replace all white-space characters with the digit "9":
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x) # Output: The9rain9in9Spain

# Example 9 : Replace the first two occurrences of a white-space character with the digit 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x) # Output: The9rain9in Spain

# Example 10 : The findall() function returns a list containing all matches.
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

# Example 10(Span) : The span() function returns a tuple containing the start-, and end positions of the match.
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span()) # Output: (12, 17)

# Example 10(String) : The string property returns the search string:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string) # Output: The rain in Spain

# Example 10(Group) : The group() method returns the part of the string where there was a match.
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group()) # Output: Spain