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


def sum_digits_in_string(input_string):
    # Initialize a variable to store the sum of digits
    digit_sum = 0
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a digit
        if char.isnumeric():
            # Convert the character to an integer and add it to the sum
            digit_sum += int(char)
    
    return digit_sum

# Get user input
user_input = input("Enter a string: ")

# Calculate the sum of digits in the input string
result = sum_digits_in_string(user_input)

# Output the result
print(f"The sum of digits in the input is: {result}")

