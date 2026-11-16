"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
#    Two string values with different capitalization: a = "vinted" and b = "Vinted".
# 2. Process:
#    - Python evaluates all six comparison operators (==, !=, <, <=, >, >=) between a and b
#      using lexicographical (Unicode code point) order.
#    - It then evaluates logical combinations (and, or, not) of those boolean comparison results.
#    - Every expression and its boolean result are formatted into aligned columns.
# 3. Out:
#    A readable, formatted table printed in the terminal showing each operator expression
#    alongside its True or False outcome.
# 4. Which two values did you pick, and which comparison result surprised you?
#    I picked a = "vinted" and b = "Vinted".
#    What surprised me is that ("vinted" > "Vinted") is True (and "vinted" < "Vinted" is False),
#    even though both represent the same word. In Python, strings are compared character by
#    character using Unicode values, where uppercase letters (ord('V') = 86) come before
#    lowercase letters (ord('v') = 118).


# Your code below
def main():
    a = "vinted"
    b = "Vinted"

    eq = a == b
    neq = a != b
    lt = a < b
    lte = a <= b
    gt = a > b
    gte = a >= b

    rows = [
        ("Comparison Operators", ""),
        (f"{a!r} == {b!r}", eq),
        (f"{a!r} != {b!r}", neq),
        (f"{a!r} <  {b!r}", lt),
        (f"{a!r} <= {b!r}", lte),
        (f"{a!r} >  {b!r}", gt),
        (f"{a!r} >= {b!r}", gte),
        ("Logical Combinations", ""),
        ("(a == b) and (a != b)", eq and neq),
        ("(a == b) or (a != b)", eq or neq),
        ("(a > b) and (a != b)", gt and neq),
        ("(a < b) or (a >= b)", lt or gte),
        ("not (a == b)", not eq),
        ("not (a > b)", not gt),
    ]

    print(f"Values: a = {a!r} (ord('v')={ord(a[0])}), b = {b!r} (ord('V')={ord(b[0])})")
    print("-" * 44)
    print(f"{'Expression':<28} | {'Result':<10}")
    print("-" * 44)

    for expr, result in rows:
        if result == "":
            print(f"\n[{expr}]")
            print("-" * 44)
        else:
            print(f"{expr:<28} | {str(result):<10}")

    print("-" * 44)


if __name__ == "__main__":
    main()
