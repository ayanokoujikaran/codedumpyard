# This file provides examples of python string methods

str = 'hello world'

# 1- length
print(len(str))

print(str.capitalize())

# 3 - count() - counts occurences of a substring
print(str.count('llo'))

# 4 - find - returns the lowest index no. of a substring, if it is not found it returns -1
# syntax - ('string', start, stop)
print(str.find('l',4,9))
  
# 5 - index() - same as find but returns value error instad of -1
print(str.index('l'))

# 6 - isalnum - checks whetherer given  string is alpha numberic
print(str.isalnum())

# 7 - isalpha - chekcs for alphabet
print(str.isalpha())

# 8 - isdigit - checks for digit
print(str.isdigit())

# 9 - islower - checks lowercase
print(str.islower())

# 10 - isupper - chekcs upppercase
print(str.isupper())

# 11 - isspace - ture if string contains whitespaces only
print(str.isspace())



# 12 - uppper converts to upppercase
print(str.upper())

# 13 - lower - converts to converts to lowercase
print(str.lower())

# 15 - strip - removes leading and trailing whitespaces
print('     hello world     '.strip())
print('     hello world     '.lstrip())
print('     hello world     '.rstrip())


# 16 - strartswith - as name suggests
print(str.startswith('hel'))

# 17 - endswith - as name suggests
print(str.endswith('rld'))

# 18 - title - turns first letter of each word of a string to uppercase
print(str.title())

# 19 - istitle -chekcs if the given string is in title format
print(str.istitle())

# 20 - replace - replaces a certain string with the given substring
# [NOTE] you can give a third argument to tell how many occurences to replace
print(str.replace('world', 'duniya'))

# 21 - join - joins a string with the each element of itereable
print('+'.join(str))
 # a better example
words = ['hello', 'how','are','you','?']
sentence = ' '.join(words)
print(sentence)

# 22 - split - splits a python string on occurence of given separator and returns a list of splitted elements
print(str.split(' '))

# 23 - partition - (gives a tuple) gandhiji's fav function, splits a string into 3 parts, middle part is the separtor itself, first and last part are the partioned parts
print(str.partition(' '))

