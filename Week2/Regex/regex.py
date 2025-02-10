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

# Example 20: Using the * meta-character which matches zero or more repetitions of the preceding regular expression
re.search('foo-*bar', 'foobar')                     # Zero dashes
# Output: <_sre.SRE_Match object; span=(0, 6), match='foobar'>
re.search('foo-*bar', 'foo-bar')                    # One dash
# Output: <_sre.SRE_Match object; span=(0, 7), match='foo-bar'>
re.search('foo-*bar', 'foo--bar')                   # Two dashes
# Output: <_sre.SRE_Match object; span=(0, 8), match='foo--bar'>

# Example 21: Using the + meta-character which matches one or more repetitions of the preceding regular expression 
re.search('foo-+bar', 'foobar')                     # Zero dashes
# Output: None
re.search('foo-+bar', 'foo-bar')                    # One dash
# Output: <_sre.SRE_Match object; span=(0, 7), match='foo-bar'>
re.search('foo-+bar', 'foo--bar')                   # Two dashes
# Output: <_sre.SRE_Match object; span=(0, 8), match='foo--bar'>

# Example 22: Using the ? meta-character which matches zero or one repetitions of the preceding regular expression
re.search('foo-?bar', 'foobar')
# Output: <_sre.SRE_Match object; span=(0, 6), match='foobar'>
re.search('foo-?bar', 'foo-bar')
# Output: <_sre.SRE_Match object; span=(0, 7), match='foo-bar'>
re.search('foo-?bar', 'foo--bar')
# Output: None

# Example 23: Greedy vs. non-greedy matching
# Greedy matching
re.search('<.*>', '%<foo> <bar> <baz>%')
# Output: <_sre.SRE_Match object; span=(1, 18), match='<foo> <bar> <baz>'>

# Non-greedy matching
re.search('<.*?>', '%<foo> <bar> <baz>%')
# Output: <_sre.SRE_Match object; span=(1, 6), match='<foo>'>
# The *? construct matches zero or more characters in a non-greedy fashion.
# Whereas the * construct matches zero or more characters in a greedy fashion.

# Example 24: Using the {m} meta-character which matches exactly m repetitions of the preceding regular expression
re.search('x-{3}x', 'x---x')
# Output: <_sre.SRE_Match object; span=(0, 5), match='x---x'>
re.search('x-{3}x', 'x--x')
# Output: None
# The regular expression x-{3}x matches exactly three dashes between the x characters.

# Example 25: Using the {m,n} meta-character which matches from m to n repetitions of the preceding regular expression
re.search('x-{1,3}x', 'x-x')
# Output: <_sre.SRE_Match object; span=(0, 3), match='x-x'>
re.search('x-{1,3}x', 'x---x')
# Output: <_sre.SRE_Match object; span=(0, 5), match='x---x'>
# The regular expression x-{1,3}x matches between one and three dashes between the x characters.

# Example 26: Using the {m,n}? meta-character which matches from m to n repetitions of the preceding regular expression in a non-greedy fashion
re.search('x-{1,3}?x', 'x---x')
# Output: <_sre.SRE_Match object; span=(0, 3), match='x-x'>
re.search('x-{1,3}?x', 'x----x')
# Output: <_sre.SRE_Match object; span=(0, 4), match='x--x'>
# The regular expression x-{1,3}?x matches between one and three dashes between the x characters in a non-greedy fashion.

# Grouping Constructs and Backreferences
# Grouping constructs allow parts of a regular expression to be treated as a single unit.
# Grouping: A group represents a single syntactic entity.
# Capturing: Some grouping constructs also capture the portion of the string that matches the subexpression inside the group.

# Example 27: Using the (...) meta-character to create a group
re.search('(bar)', 'foo bar baz')
# Output: <_sre.SRE_Match object; span=(4, 7), match='bar'>
re.search('(bar)+', 'foo barbar baz')
# Output: <_sre.SRE_Match object; span=(4, 10), match='barbar'>
re.search('(\w+),(\w+),(\w+)', 'foo,quux,baz')
# Output: <_sre.SRE_Match object; span=(0, 12), match='foo,quux,baz'>
# The regular expression (\w+),(\w+),(\w+) matches three words separated by commas.
groupings = re.search('(\w+),(\w+),(\w+)', 'foo,quux,baz')
print(groupings.group(0)) # Output: foo,quux,baz
print(groupings.group(1)) # Output: foo
print(groupings.group(2)) # Output: quux
print(groupings.group(3)) # Output: baz

# Backreferences: A backreference allows a previously matched group to be matched again.
# Example 28: Using the \1 meta-character to match the same text as most recently matched by the 1st capturing group
regex = r'(\w+),\1'
re.search(regex, 'foo,foo')
# Output: <_sre.SRE_Match object; span=(0, 7), match='foo,foo'>
# Using regex as a variable to store the regular expression.

# Example 29: Using the (?P<name>...) meta-character to create a named group
m = re.search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,quux,baz')
print(m.group('w1')) # Output: foo
print(m.group('w2')) # Output: quux
print(m.group('w3')) # Output: baz
# The regular expression (?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+) matches three words separated by commas.
# The named groups are w1, w2, and w3.

# Example 30: Using the (?P=name) meta-character to match the same text as most recently matched by the named group name
regex = r'(?P<word>\w+),(?P=word)'
re.search(regex, 'foo,foo')
# Output: <_sre.SRE_Match object; span=(0, 7), match='foo,foo'>
# The regular expression (?P<word>\w+),(?P=word) matches the same word separated by a comma.

# Example 31: Using the (?:...) meta-character to create a non-capturing group
m = re.search('(\w+),(?:\w+),(\w+)', 'foo,quux,baz')
print(m.groups()) # Output: ('foo', 'baz')
# The regular expression (\w+),(?:\w+),(\w+) matches three words separated by commas.
# The middle word is not captured.
m.group(0) # Output: 'foo,quux,baz'
m.group(1) # Output: 'foo'
m.group(2) # Output: 'baz'

# Example 32: Using the (?(<n>)<yes-regex>|<no-regex>) meta-character to match the yes-regex if the n-th capturing group has matched, else match the no-regex
re.search(r'(?:(\d+)|(\w+))', '123')
# Output: <_sre.SRE_Match object; span=(0, 3), match='123'>
re.search(r'(?:(\d+)|(\w+))', 'abc')
# Output: <_sre.SRE_Match object; span=(0, 3), match='abc'>
# The regular expression (?:(\d+)|(\w+)) matches either one or more digits or one or more word characters.

# Example 33: Lookahead and Lookbehind Assertions
# Lookahead: A lookahead assertion is used to match a pattern only if it’s followed by another pattern.
# Lookbehind: A lookbehind assertion is used to match a pattern only if it’s preceded by another pattern.

re.search('foo(?=[a-z])', 'foobar')
# The lookahead expression foo(?=[a-z]) matches foo only if it’s followed by a lowercase letter.
# Output: <_sre.SRE_Match object; span=(0, 3), match='foo'>
re.search('(?<=[a-z])bar', 'foobar')
# Output: <_sre.SRE_Match object; span=(3, 6), match='bar'> 
# The lookbehind expression (?<=[a-z])bar matches bar only if it’s preceded by a lowercase letter.

# Example 34: Using the (?<!<lookbehind_regex>) meta-character to match if the current position in the string is not preceded by a match of <lookbehind_regex>
re.search('(?<!foo)bar', 'foobar')
# Output: None
# The lookbehind expression (?<!foo)bar matches bar only if it’s not preceded by foo.

# Example 35: Using the (?#...) meta-character to add comments to a regular expression
re.search('bar(?#This is a comment) *baz', 'foo bar baz qux')
# Output: <_sre.SRE_Match object; span=(4, 10), match='bar baz'>

# Example 36: Using the | meta-character to match either the regular expression preceding or following it
re.search('foo|bar|baz', 'bar')
# Output: <_sre.SRE_Match object; span=(0, 3), match='bar'>
re.search('foo|bar|baz', 'quux')