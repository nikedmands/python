import re

# variables
# r means raw string literal. i.e. treat \ as a literal character
pattern = r'ab'
text = 'abc acb'
# matches variable, findall in re library - searches sting for matching pattern
matches = re.findall(pattern, text)
# f string, interpolates variable into a string
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")

# . match any single character
pattern = r'.'
text = 'abcdef'
matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")

# \d looks for how many single digit entities
pattern = r'\d'
text = 'FirstWord 1 LastWord'
matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")

# \D looks for non-single digit characters. opposite of above
pattern = r'\D'
text = 'FirstWord 1 LastWord'
matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")

# \w matches word characters
pattern = r'\w'
text = 'FirstWord 1 LastWord'
matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")

# matches whitespace
pattern = r'\s'
text = 'FirstWord 1 LastWord'
matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")

1
2
# \w+ match one or more word characters
pattern = r'\w+'
text = 'FirstWord 1 LastWord'
matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")

# match items in the range of characters
1
2
pattern = r'[4-6]'
text = '123456789'
matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")

# matches one or more characters of the range
1
2
pattern = r'[4-6]+'
text = '123456789'
matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")

# match the range as one or more characters
1
2
pattern = r'[d-f]+'
text = 'abcdefghi'
matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")

# matches groups of characters, separated by the ! and ?
1
2
pattern = r'[a-z0-9]+'
text = 'word!1234?wordandletters'
matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")

# matches groups including consonants and spaces, but not the vowels.
1
2
pattern = r'[^aeuio]+'
text = 'The quick brown fox jumps over the lazy dog.'
matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")