text = input("Please type a string. ")
print(f"This is your string in all upper case: {text.upper()}")
print(f"This is your string in all lower case: {text.lower()}")
print(f"This is your string in 'title' case: {text.title()}")

alpha = 0
number = 0

#look at each character in the string. Use the string inputed from above.
for h in text:
    if h.isalpha():
        alpha = alpha+1
    if h.isnumeric():
        number = number+1

print(f'We looked through "{text}" and found:')
print(f'{alpha} alphabet characters')
print(f'{number} numeric characters')

