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

# 1. In: An integer N typed by the user.
# 2. Process: Ask for input, validate range (1 to 100 max), then loop from 1 to N and check modulo % 2 for each number.
# 3. Out: For each number from 1 to N, print whether it is odd or even.
# 4. What happens on 0, on a negative number, on a very large number:
#    - 0 or negative number: Display an error message asking for a positive number >= 1.
#    - Very large number (> 100, e.g. 5000): Display a limit message capping execution to avoid spamming the terminal.

# Check it yourself results:
# - Tested with 6: Printed exactly 3 odd numbers (1, 3, 5) and 3 even numbers (2, 4, 6).
# - Tested with 0 or negative (-4): Displayed "Please enter an integer greater than 0."
# - Tested with 5000: Displayed "Number is too large! Please enter a number between 1 and 100."


# Your code below

# Asking user for an integer N
n_str = input("Enter an integer N: ")
n = int(n_str)

# Validating input decisions
if n <= 0:
    print("Please enter an integer greater than 0.")
elif n > 100:
    print("Number is too large! Please enter a number between 1 and 100.")
else:
# Loop from 1 to N to check odd/even
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(f"{i} is Even")
        else:
            print(f"{i} is Odd")