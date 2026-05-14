# Today we are learning about Strings
my_str_1 = 'Hello people'
my_str_2 = "Hello people"

str_1 = "John said, 'Go away!'"
str_2 = 'Carla said, "Never!!"'

multi_string = '''This is a multi 
line string. Deal with it.'''

#print('Hello' in my_str_1) # True
#print('e' in my_str_1) # True
#print('What' in my_str_1) # False

New_str = 'Axialradiationjuveniledetention center'
#print(len(New_str)) 

#print(my_str_1[-2])
#print(my_str_1[0:5])
 
#greeting = 'Hi'
#greeting = 'Hey there' # Strings are immutable, but can be reassigned to a new variable

#print(greeting)

#str_plus = str_1 + '' + str_2 # String Concatenation
# print(str_plus)


name = 'Stefan Mathew'
age = 23
name_age = f'My name is {name} and I am {age} years old'

grade1 = 50
grade2 = 75

result = f'My name is {name} and I scored {grade1} in Mechanics and {grade2} in Aerospace Structures'
#print(result[::-1])

str_a = 'Hello world'
up_str_a = str_a.upper()
low_str_a = str_a.lower()

trim_str = str_a.strip()

#split_str = result.split()
#print(split_str)

#new_list = ['Max', 'imum', 'occu', 'pancy','120']
#joined_str = ''.join(new_list)
#print(joined_str)

starts_w = str_a.startswith('Nein')
ends_w = str_a.endswith('ld')
#print(ends_w)

str_index = str_a.find('world')
#print(str_index)

count_str = result.count('a')
#print(count_str)

Random_string = 'humungous'
cap_str = Random_string.capitalize()
print(cap_str)

#result = result.upper()
is_all_upper = result.isupper()
#print(is_all_upper)

result = result.title()
print(result)