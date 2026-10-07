"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Two numbers typed by the user (converted to float).
# 2. Process: Ask for inputs, convert strings to float, calculate addition, subtraction, multiplication, and division.
# 3. Out: Results of the 4 basic mathematical operations displayed in the terminal.
# 4. What happens when the second number is zero, and why:
#    I decided to display a clear error message instead of dividing by zero to prevent a ZeroDivisionError crash.

# Check it yourself results:
# - Tested with 7 and 2:
#   7 + 2 = 9.0 | 7 - 2 = 5.0 | 7 * 2 = 14.0 | 7 / 2 = 3.5
#   Reason for result: Python 3 uses `/` for standard float division, which gives 3.5. If integer division `//` were used, it would output 3 by rounding down.
# - Tested with 0 as second number:
#   Displays: "Division: Division by zero is not allowed." without crashing.


# Your code below

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

if num2 == 0:
    print("Division: Division by zero is not allowed.")
else:
    print(f"{num1} / {num2} = {num1 / num2}")