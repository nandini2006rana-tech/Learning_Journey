info = 'python is important now days'
print('now'in info)
# we can also find out particular word indexing with the help of find()

print(info.find('now'))
print(info.find('PYTHON'))

# find() does not return error instead of that it will give you -1 in output.
'''to import regex we have to write 
 import re'''
import re
'''in code to find out something we can use indexing , find() function and in regex we have a re.search() who looks anywhere in the string to find out alphabet or numbers but also gives 
 more information than that like it will give you indexing as span and match.'''
here =(re.search('important',info))
print(here)
text = "Hello Nandini 2026 Nandini"

# remember the pattern used in re.search is (pattern,string)

you = re.search("[0-9][.][0-9][0-9]", text)
print(you)

'''here .(dot) is a meta character means special character in regex, it means dot will count as any character except new line character (\n)
but if we use like this [.] then it means it will match only to dot in a string'''
#here re.search tool looks only first occurrence .

a = 'I am working on my skills3.0'
b = r'[a-z][a-z]'
# To avoid special characters which we don't want but there in somehow we have to use that symbols then we use r outside the string so that special characters will not used .
c = re.search('[a-z][a-z]', a)
print(c)
# \d means any digit.It is similar to [0-9] or[0123456789]
b = r'[a-z][a-z]\d'
c = re.search(b,a)
print(c)
#\D means any non character digit.For eg: any a-z.
b = r'[a-z][a-z]\D'
c = re.search(b,a)
print(c)
# \s means white space, new line and \t(it means creates a space similar to pressing the Tab key on your keyboard)

new_line = "I may not available tomorrow evening 5'o clock"
u = r'[a-z][a-z][a-z]\s'
v= re.search(u,new_line)
print(v)
# \S is opposite to \s means it will gives any character.

# \w represents [a-z],[A-Z],[0-9],_(underscore).
leo = "I can't able to find a file having name python_work "
i = r'[a-z][a-z][a-z][_]\w'
o =re.search(i,leo)
print(o)
# \W is opposite of \w

# Quantifiers tell us how many times a character or pattern should occur.
# Quantifiers are +(it shows one or more time),
# *(means 0 or more time), ?(means 0 or 1 time),{n}(means n number of time)

y = 'I love to eat Ice Cream'
k= r'[A-Z][a-z]{4}'
j =re.search(k,y)
print(j)
# In above example the quantifier {4} will applied on [a-z].

y = 'I love to eat Ice Cream'
k= r'[A-Z][a-z]{2,5}'
j =re.search(k,y)
print(j)
# {2,5} means min 2 character and max 5 character.

y = 'I love to eat Ice Cream'
k= r'[A-Z]+'
j =re.search(k,y)
print(j)

# ^ is a caret. If we use this outside the bracket it means found something which is in starting but if we use inside the bracket then it means found except the given number or alphabet.
sentence = 'Today I would like to eat something spicy.'
make = r'^[A-Z][a-z]{4}'
match_object = re.search(make,sentence)
print(match_object)

sentence = 'Today I would like to eat something spicy.'
make = r'[^A-Z][a-z]{4}'
match_object = re.search(make,sentence)
print(match_object)
# In above code it will give none because ^ caret finds beginning of the string.

# $ it finds from ending part of the string .
sentence = 'Today I would like to eat something spicy'
make = r'[a-z]{5}$'
match_object = re.search(make,sentence)
print(match_object)

# ()group = it uses to match words or number in a string
# | = it works like or
sen1 = 'I am hungry'
make = r'(am|hungry)'
match_object1 = re.search(make,sen1)
print(match_object1)
# [] square bracket use to match or find a single occurrence of a word or number.

# re.match() checks only from the beginning of the string.
sen1 = 'I am hungry'
make = r'[a-z]{3}'
match_object1 = re.match(make,sen1)
print(match_object1)

# re.findall() is used when you want to find all the matches of a pattern in a string.
roll_no = '23,34,45,56,90,09'
pattern = r'[0-9]{2}'
match = re.findall(pattern,roll_no)
print(match)
# re.findall() never gives you none instant of that it will give you empty list [].
phone = '123456,78901,1234567890,5958358032,553989034,ice-2'
pattern = r'[0-9]{6,}'
match = re.findall(pattern,phone)
print(match)
# {6,} shows min limit count is 6 and no maximum limit.

# \b means word or number boundary.
phone = '123456,78901,1234567890,5958358032,553989034,ice-2'
pattern = r'[0-9]{6,10}\b'
match = re.findall(pattern,phone)
print(match)

