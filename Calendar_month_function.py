def get_month(input_number):
    '''Takes a number between 1 and 12 from the user
    and converts that to a corresponding month of the year.'''

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    if 1 <= input_number <= 12:
        return months[input_number - 1]
    else:
        return "Please input a number between 1 and 12. "

user_input = int(input("Enter a number between 1 and 12: "))
result = get_month(user_input)
print(f"Your input corresponds to the month of {result}")
