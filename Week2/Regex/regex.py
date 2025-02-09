# Example 1: Using the in operator
s = 'foo123bar'
print('123' in s) # Output: True

# Example 2: Using the find() method
s = 'foo123bar'
print(s.find('123')) # Output: 3

# Example 3: Using the index() method
s = 'foo123bar'
print(s.index('123')) # Output: 3

# Example 4: Using the re module
import re
s = 'foo123bar'
print(re.search('123', s)) # Output: <re.Match object; span=(3, 6), match='123'>
# Returned a match object rather than None.

# Because a match object is truthy, it can be used in conditional statements.
if re.search('123', s):
     print('Found a match.')
else:
    print('No match.')
# Output: Found a match.

# Example 5: Using the re search() method
re.search('[0-9][0-9][0-9]', 'foo456bar')
# Output: <re.Match object; span=(3, 6), match='456'>
# The regular expression [0-9][0-9][0-9] matches any sequence of three digits.
print(re.search('[0-9][0-9][0-9]', '12foo34')) # Output: None
# The regular expression [0-9][0-9][0-9] does not match three consecutive digits in the string '12foo34'

# Example 6: Using the . meta-character which matches any character except a newline character
# The . meta-character matches any character except a newline character.

s = 'foo123bar'
print(re.search('1.3', s)) # Output: True
# Output: <re.Match object; span=(3, 6), match='123'>

# Example 7: Using the [] meta-character which matches any character inside the square brackets
re.search('ba[artz]', 'foobarqux')
# Output: <re.Match object; span=(3, 6), match='bar'>

# Example 8: Using the - meta-character to specify a range of characters
re.search('[a-z]', 'FOObar')
# Output: <re.Match object; span=(3, 4), match='b'>
re.search('[a-z][a-z][a-z]', 'FOObar')
# Output: <re.Match object; span=(3, 6), match='bar'>

# Example 9: Using the ^ meta-character which matches any character that isn’t in the set i.e
re.search('[^0-9]', '12345foo')
# Output: <re.Match object; span=(5, 6), match='f'>

# Example 10: Using the \w meta-character which matches any alphanumeric character
re.search('\w', '#(.a$@&')
# Output: <re.Match object; span=(3, 4), match='a'> a being the first alphanumeric character

# Example 11: Using the \W meta-character which matches any non-alphanumeric character
re.search('\W', 'a_1*3Qb')
# Output: <re.Match object; span=(3, 4), match='*'> * being the first non-alphanumeric character

# Example 12: Using the \d meta-character which matches any digit
re.search('\d', 'abc4def')
# Output: <re.Match object; span=(3, 4), match='4'> 4 being the first digit

# Example 13: Using the \D meta-character which matches any non-digit
re.search('\D', '234Q678')
# Output: <re.Match object; span=(3, 4), match='Q'> Q being the first non-digit

# Example 14: Using the \s meta-character which matches any whitespace character
re.search('\s', 'foo\nbar baz')
# Output: <re.Match object; span=(3, 4), match='\n'> \n being the first whitespace character

# Example 15: Using the \S meta-character which matches any non-whitespace character
re.search('\S', '  \n foo  \n  ')
# Output: <re.Match object; span=(4, 5), match='f'> f being the first non-whitespace character

# Example 16: Using the ^ or /A meta-character which matches the start of a string
re.search('^foo', 'foobar')
# Output: <re.Match object; span=(0, 3), match='foo'>
re.search('\Afoo', 'foobar')
# Output: <re.Match object; span=(0, 3), match='foo'>
re.search('^foo', 'barfoo')
# Output: None

# Example 17: Using the $ or /Z meta-character which matches the end of a string
re.search('bar$', 'foobar')
# Output: <re.Match object; span=(3, 6), match='bar'>
re.search('bar\Z', 'foobar')
# Output: <re.Match object; span=(3, 6), match='bar'>
re.search('bar$', 'barfoo')
# Output: None

# Example 18: Using the \b meta-character which matches if a string is at the beginning or end of a word
re.search(r'\bbar', 'foo bar')
# Output: <re.Match object; span=(4, 7), match='bar'>
re.search(r'\bbar', 'foobar')
# Output: None

# Example 19: Using the \B meta-character which matches if a string is not at the beginning or end of a word
re.search(r'\Bfoo\B', 'barfoobaz')
# Output: <re.Match object; span=(3, 6), match='foo'>