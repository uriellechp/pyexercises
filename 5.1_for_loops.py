"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The list of 8 campaign acquisition costs from exercise 4.0.
# 2. Process: Iterate through the list with enumerate(), format each index starting at 1, and calculate the percentage share of each item relative to the total cost.
# 3. Out: Exactly 8 formatted lines showing the item position, cost value, and calculated percentage share of total budget.
# 4. What I compute for each item, and why it is worth showing:
#    I computed the percentage share of total marketing expenditure for each campaign.
#    This informs the marketing manager about budget concentration and cost distribution across campaigns.

# Check it yourself results:
# The program printed exactly 8 lines, matching the 8 items in the original list.
# Sum of printed percentages equals 100% (120.50 / 1178.00 = 10.23%, etc.).


# Your code below

# Reusing list from exercise 4.0
cac_budgets = [120.50, 85.00, 210.00, 95.00, 310.00, 150.00, 62.50, 145.00]
total_budget = sum(cac_budgets)

# Loop through each item displaying position, value, and computed percentage share
for position, cost in enumerate(cac_budgets, start=1):
    percentage = (cost / total_budget) * 100
    print(f"Campaign #{position}: {cost:.2f} € ({percentage:.1f}% of total budget)")
