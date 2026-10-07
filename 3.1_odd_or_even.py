"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A positive integer N typed by the user.
# 2. Process: Convert input to int, validate edge cases, and loop from 1 to N using modulo (%) to check if each number is odd or even.
# 3. Out: Messages indicating whether each number from 1 to N is odd or even, or an error message for invalid inputs.
# 4. What happens on 0, on a negative number, on a very large number:
#    - On 0: Displays an error message stating that N must be a positive integer >= 1.
#    - On negative numbers: Displays an error message stating that N must be a positive integer >= 1.
#    - On 5000 (or > 100): Displays a warning message refusing values over 100 to avoid flooding the terminal.

# Check it yourself results:
# - Tested with 6: Correctly outputs 3 odd (1, 3, 5) and 3 even (2, 4, 6) lines.
# - Tested with 0: Displays "Error: Please enter a positive integer greater than 0."
# - Tested with -4: Displays "Error: Please enter a positive integer greater than 0."
# - Tested with 5000: Displays "Error: Number too large. Please enter a number <= 100."


# Your code below

# Asking user for an integer N
user_input = input("Enter a positive number N: ")
N = int(user_input)

# Edge case checks
if N <= 0:
    print("Error: Please enter a positive integer greater than 0.")
elif N > 100:
    print("Error: Number too large. Please enter a number <= 100.")
else:
    # Loop from 1 to N
    for i in range(1, N + 1):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")