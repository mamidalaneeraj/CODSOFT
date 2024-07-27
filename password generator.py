import random
import string

print('welcome to random password generator')
print('------------------------------------')
print('This program will generate random password according to the length of the password selected')

# getting the required length from user
length=int(input('enter the length of the password '))

# using string module to import all lettrs,numbers and special characters
letters=string.ascii_letters
numbers=string.digits
symbols=string.punctuation

# combining in single variable
combo=letters+numbers+symbols

# creating  varible to randomly selet the characters
y=random.sample(combo,length)

# using 'join' to join all characters selected
password=''.join(y)
print(f'the generated password of length {length} is {password} ')