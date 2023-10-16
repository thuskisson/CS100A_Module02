def sum_digits_in_string(input_string):
    # Initialize a variable to store the sum of digits
    digit_sum = 0
    
    # Iterate through each character in the input string
    for num in input_string:
        # Check if the character is a digit
        if num.isnumeric():
            # Convert the character to an integer and add it to the sum
            digit_sum += int(num)
    
    return digit_sum

# Get user input
user_input = input("Enter a string: ")

# Calculate the sum of digits in the input string
result = sum_digits_in_string(user_input)

# Output the result
print(f"The sum of digits in the input is: {result}")