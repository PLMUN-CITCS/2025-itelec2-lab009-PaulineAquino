# if_else_statement.py

# Optional: Wrap your code in a try-except block to handle non-integer inputs.
try:
    # 1. Prompt the user for a number and store it in a variable.
    user_input = input("Enter a number: ")

    # 2. Convert the user input from a string to an integer.
    number = int(user_input)

    # 3. Check if the number is even or odd using the modulus operator.
    if number % 2 == 0:
        print(f"The number {number} is Even.")
    else:
        print(f"The number {number} is Odd.")

# This block will catch cases where the user does not enter a valid integer.
except ValueError:
    print("Invalid input. Please enter an integer.")
