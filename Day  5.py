# Boolean Operators and Conditionals
#print(bool(''))
#print(bool(5))

#print(bool(1))
#print(bool(True))

is_geek = True
age = 23

print(is_geek and age) ''' And operator checks from left to right and returns the 
second operand if the first operand is true'''

if is_geek and age >= 18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')



