"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A sentence typed by the user (string).
# 2. Process: Ask for input, then apply four string methods (.upper(), .lower(), .strip(), and .title()).
# 3. Out: Four modified versions of the user's sentence printed on separate lines.
# 4. My four transformations, and when each is useful:
#    - upper(): Useful for highlighting titles or urgent warning messages in a report.
#    - lower(): Useful for standardizing user input like email addresses before saving them.
#    - strip(): Useful for cleaning spaces accidentally added at the start or end of a form field.
#    - title(): Useful for formatting full names or job titles correctly with proper capitalization.

# Check it yourself result (Tested with "  hello World  "):
# - upper(): "  HELLO WORLD  " -> Yes, expected (converts all letters to uppercase).
# - lower(): "  hello world  " -> Yes, expected (converts all letters to lowercase).
# - strip(): "hello World" -> Yes, expected (removes spaces at start and end).
# - title(): "  Hello World  " -> Yes, expected (capitalizes the first letter of each word).


# Your code below

# Asking user for text input
user_sentence = input("Please enter a sentence: ")

# Displaying 4 transformed versions
print("1. Uppercase:", user_sentence.upper())
print("2. Lowercase:", user_sentence.lower())
print("3. Stripped spaces:", user_sentence.strip())
print("4. Title case:", user_sentence.title())
