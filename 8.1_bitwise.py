"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
#    Four integer bitmasks representing individual permissions for managing an online resale shop:
#    - VIEW_INVENTORY  = 0b0001 (1) : view listed items and stock
#    - EDIT_PRICES     = 0b0010 (2) : change item prices and descriptions
#    - PUBLISH_LISTING = 0b0100 (4) : publish new items live to buyers
#    - ISSUE_REFUND    = 0b1000 (8) : approve buyer returns and issue refunds
# 2. Process:
#    - Combine VIEW_INVENTORY and EDIT_PRICES using bitwise OR (|) to create a junior assistant role.
#    - Test whether PUBLISH_LISTING is present in the role using bitwise AND (&).
#    - Add PUBLISH_LISTING to the role using bitwise OR assignment (|=).
#    - Remove EDIT_PRICES from the role using bitwise AND with bitwise NOT (&= ~).
# 3. Out:
#    Printed output at each step showing the role's permissions in 4-bit binary format (e.g., 0b0011)
#    along with the boolean check result so each bit change can be read directly.
# 4. What are your permissions about?
#    They represent access rights for team members helping manage a secondhand clothing store
#    (such as a Vinted/Depop shop): viewing stock, editing prices, publishing new listings live,
#    and issuing customer refunds.


# Your code below
VIEW_INVENTORY = 0b0001   # 1 (bit 0)
EDIT_PRICES = 0b0010      # 2 (bit 1)
PUBLISH_LISTING = 0b0100  # 4 (bit 2)
ISSUE_REFUND = 0b1000     # 8 (bit 3)


def format_bits(value):
    return f"0b{value:04b} (decimal {value})"


def main():
    print("Base permissions:")
    print(f"  VIEW_INVENTORY  = {format_bits(VIEW_INVENTORY)}")
    print(f"  EDIT_PRICES     = {format_bits(EDIT_PRICES)}")
    print(f"  PUBLISH_LISTING = {format_bits(PUBLISH_LISTING)}")
    print(f"  ISSUE_REFUND    = {format_bits(ISSUE_REFUND)}\n")

    # Step 1: Combine two permissions (VIEW_INVENTORY | EDIT_PRICES)
    role_perms = VIEW_INVENTORY | EDIT_PRICES
    print(f"1. Combined VIEW + EDIT       -> {format_bits(role_perms)}")

    # Step 2: Test whether a third permission (PUBLISH_LISTING) is present
    has_publish = bool(role_perms & PUBLISH_LISTING)
    print(f"2. Has PUBLISH_LISTING?       -> {has_publish} ({format_bits(role_perms)})")

    # Step 3: Add PUBLISH_LISTING using bitwise OR (|=)
    role_perms |= PUBLISH_LISTING
    print(f"3. Added PUBLISH_LISTING      -> {format_bits(role_perms)}")

    # Step 4: Remove EDIT_PRICES using bitwise AND + NOT (&= ~)
    role_perms &= ~EDIT_PRICES
    print(f"4. Removed EDIT_PRICES        -> {format_bits(role_perms)}")


if __name__ == "__main__":
    main()
