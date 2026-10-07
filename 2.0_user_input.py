"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Two user inputs (company name as text and budget in euros as a number).
# 2. Process: Ask for inputs, convert budget to float, calculate total with 20% VAT, and format output sentence.
# 3. Out: A quote sentence displaying the company name and total budget including VAT.
# 4. My two fields, and what I would do with them: Company name and budget. Used in business to calculate quote prices with taxes.

# Check it yourself results:
# - Empty line: Accepts empty string for company name; crashes with ValueError when converting empty text to float.
# - Space: Accepts space as string; crashes with ValueError when converting space to float.
# - Text instead of number: Crashes with ValueError because non-numeric text cannot be converted to float.


# Your code below

# Asking the user for client name and budget
company_name = input("Enter client company name: ")
budget_str = input("Enter project budget (in €): ")

# Converting budget string to float to compute tax
budget = float(budget_str)
total_with_vat = budget * 1.20

# Displaying final sentence
print(f"Project quote for {company_name}: {total_with_vat:.2f} € (VAT included).")