"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
#    Three text inputs typed by the user in the terminal for a resale order record:
#    - Order ID (order_id)
#    - Buyer Email (buyer_email)
#    - French Postal Code (postal_code)
# 2. Process:
#    - Leading and trailing spaces are stripped from each input.
#    - Each field is checked against its specific regular expression using re.fullmatch(),
#      which forces the ENTIRE string (not just a substring) to match the rule.
#    - If a field fails validation, the user is told why and re-prompted until it matches.
#    - Only when ALL three fields pass validation are they saved together to "validated_orders.txt".
# 3. Out:
#    Confirmation printed in the terminal and one clean line appended to "validated_orders.txt"
#    (e.g., "VNT-2026-0412 | claire.martin@skema.edu | 91150").
# 4. What are your three fields, and what makes a value acceptable for each? (Plain English rules)
#    - Field 1 — Order ID:
#      Must start with the exact uppercase prefix "VNT-", followed by a 4-digit year starting with
#      "20" (e.g., 2026), a hyphen "-", and exactly 4 digits (e.g., "VNT-2026-0412").
#      Rejects lowercase ("vnt-2026-0412"), wrong year format ("VNT-26-0412"), or wrong digit counts.
#    - Field 2 — Buyer Email:
#      Must have a local username before "@" made only of lowercase/uppercase letters, digits, dots,
#      underscores, or hyphens (cannot start or end with a dot), followed by "@", a domain name with
#      letters/digits/hyphens, a dot ".", and a 2-to-4 letter extension (e.g., "alice.dupont@gmail.com").
#      Rejects missing "@", spaces, double dots ("alice..dupont@gmail.com"), or single-letter TLDs.
#    - Field 3 — French Postal Code:
#      Must be exactly 5 digits starting with "01" through "95" (mainland France departments) or
#      "97" / "98" (overseas territories). Rejects "00000", "96123", "99000", 4-digit codes, or letters.


# Your code below
import re

# --- Regex 1: Order ID ---
# Piece-by-piece explanation in my own words:
#   ^         -> start of the string
#   VNT-      -> exact literal uppercase text "VNT-"
#   20\d{2}   -> literal "20" followed by any 2 digits (years 2000 to 2099)
#   -         -> literal hyphen "-"
#   \d{4}     -> exactly 4 digits (0000 to 9999)
#   $         -> end of the string
ORDER_ID_PATTERN = re.compile(r"^VNT-20\d{2}-\d{4}$")

# --- Regex 2: Buyer Email ---
# Piece-by-piece explanation in my own words:
#   ^                          -> start of the string
#   [A-Za-z0-9_-]+             -> one or more letters, digits, underscores, or hyphens (username start)
#   (?:\.[A-Za-z0-9_-]+)*     -> optional dot-separated segments (prevents leading, trailing, or double dots)
#   @                          -> literal "@" symbol
#   [A-Za-z0-9-]+              -> domain name (letters, digits, or hyphens)
#   (?:\.[A-Za-z0-9-]+)*       -> optional subdomain(s) like ".edu" before the final TLD
#   \.[A-Za-z]{2,4}            -> a literal dot followed by 2 to 4 letters (e.g., .fr, .com, .info)
#   $                          -> end of the string
EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,4}$")

# --- Regex 3: French Postal Code ---
# Piece-by-piece explanation in my own words:
#   ^                                  -> start of the string
#   (?:0[1-9]|[1-8]\d|9[0-5]|97|98)    -> first 2 digits must be 01-09, 10-89, 90-95, 97, or 98 (excludes 00, 96, 99)
#   \d{3}                              -> followed by any 3 digits
#   $                                  -> end of the string
POSTAL_CODE_PATTERN = re.compile(r"^(?:0[1-9]|[1-8]\d|9[0-5]|97|98)\d{3}$")


def prompt_valid_field(prompt_text, pattern, error_hint):
    while True:
        user_value = input(prompt_text).strip()
        if pattern.fullmatch(user_value):
            return user_value
        print(f"Invalid format: {error_hint}\n")


def main():
    print("=== Resale Order Registration ===")
    order_id = prompt_valid_field(
        "Order ID (e.g., VNT-2026-0412): ",
        ORDER_ID_PATTERN,
        "Must match VNT-20YY-XXXX (uppercase VNT, 4-digit year starting with 20, 4-digit number).",
    )
    buyer_email = prompt_valid_field(
        "Buyer Email (e.g., claire.martin@gmail.com): ",
        EMAIL_PATTERN,
        "Must be a valid email (user@domain.ext, no spaces or consecutive dots).",
    )
    postal_code = prompt_valid_field(
        "French Postal Code (e.g., 91150): ",
        POSTAL_CODE_PATTERN,
        "Must be 5 digits starting with a valid French department code (01-95, 97, or 98).",
    )

    record = f"{order_id} | {buyer_email} | {postal_code}\n"
    with open("validated_orders.txt", mode="a", encoding="utf-8") as out_file:
        out_file.write(record)

    print(f"\nAll three fields validated and saved: {record.strip()}")


if __name__ == "__main__":
    main()


# --- CHECK IT YOURSELF: 9 test values (1 pass + 2 fail per field) ---
# Field 1 (Order ID):
#   - PASS: "VNT-2026-0412" -> accepted immediately.
#   - FAIL 1: "vnt-2026-0412"
