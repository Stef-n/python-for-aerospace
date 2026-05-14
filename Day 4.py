# Day 4

#print(14>=4)

age = int(input("Enter your age:"))
if age >= 18:
    print("You are a young adult")
elif age >= 65:
    print("You are a senior citizen")
elif age >= 30:
    print("You are an adult in their prime")
elif age >= 13:
    print("You are a teenager")
elif age >= 4:
    print("You are a child")
else:
    print("You are a toddler!")
