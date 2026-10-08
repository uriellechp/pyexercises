"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The list of marketing campaign acquisition costs from exercise 4.0.
# 2. Process: Display the list in 4 different orders using both non-destructive methods (sorted, reversed) and temporary copies before using in-place methods (.sort(), .reverse()).
# 3. Out: Four different orderings displayed, followed by the original intact list.
# 4. My four orders, and which ones modify the original:
#    - Ascending order (sorted()): Does NOT modify original (returns a new list).
#    - Descending order (sorted(..., reverse=True)): Does NOT modify original (returns a new list).
#    - Reversed order (list(reversed())): Does NOT modify original (returns an iterator converted to a new list).
#    - In-place sorted (.sort()): WOULD modify original, so applied on a copy (.copy()) to preserve the original.

# Check it yourself results:
# The original list at the end is [120.5, 85.0, 210.0, 95.0, 310.0, 150.0, 62.5, 145.0].
# It matches item by item the initial list defined in exercise 4.0.


# Your code below

# Original list from exercise 4.0
cac_budgets = [120.50, 85.00, 210.00, 95.00, 310.00, 150.00, 62.50, 145.00]

# Order 1: Ascending order (using sorted - non-destructive)
print("1. Ascending order:", sorted(cac_budgets))

# Order 2: Descending order (using sorted with reverse=True - non-destructive)
print("2. Descending order:", sorted(cac_budgets, reverse=True))

# Order 3: Reversed order (using reversed() - non-destructive)
print("3. Reversed order:", list(reversed(cac_budgets)))

# Order 4: In-place sorted on a explicit copy to protect the original
cac_copy = cac_budgets.copy()
cac_copy.sort()
print("4. In-place sorted copy:", cac_copy)

# Proof that original list is intact
print("Original list unchanged proof:", cac_budgets)