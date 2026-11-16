"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
#    A fixed marketing campaign budget in euros (budget = 1200.0) and the number of conversions
#    entered by the user as text in the terminal (e.g., "25", "0", "abc", or "").
# 2. Process:
#    - The program loops up to a maximum of 5 attempts (MAX_ATTEMPTS = 5) so it never loops infinitely
#      if a user keeps entering invalid data, while still surviving every bad input without crashing.
#    - It strips whitespace and attempts to convert the user's input into a float.
#    - It then divides the total campaign budget by the number of conversions to compute Cost Per Acquisition (CPA).
#    - Separate except blocks handle ValueError (non-numeric or empty input) and ZeroDivisionError (0 conversions).
# 3. Out:
#    Either the calculated Cost Per Acquisition (e.g., "Cost per conversion: 48.00 EUR") on valid input,
#    a specific error message explaining why the input failed, or a polite stop message after 5 failed attempts.
# 4. The two failures, and whether they deserve the same message:
#    - Failure 1 (ValueError): happens when the user enters non-numeric text like "abc" or an empty line "".
#    - Failure 2 (ZeroDivisionError): happens when the user enters 0 (or 0.0), which is a valid number
#      but cannot be used as a divisor.
#    - Should they produce the same message? No. Telling a user "0 is not a valid number" is confusing
#      because 0 IS a number; they need to know that zero conversions cannot be divided by, whereas
#      typing "abc" or pressing Enter requires asking for a numeric value.
#    - Why catching each failure separately is better than catching Exception at once:
#      A single broad "except Exception:" hides what actually went wrong, forces a vague generic message
#      for the user, and can silently mask real programming bugs (like a typo in a variable name, NameError)
#      instead of letting us fix them.


# Your code below
MAX_ATTEMPTS = 5


def main():
    total_budget = 1200.0
    attempts = 0

    print(f"Campaign Budget: {total_budget:.2f} EUR")
    print(f"You have up to {MAX_ATTEMPTS} attempts to enter a valid conversion count.\n")

    while attempts < MAX_ATTEMPTS:
        raw_input = input("Enter number of conversions: ").strip()
        attempts += 1

        try:
            conversions = float(raw_input)
            cost_per_conversion = total_budget / conversions
        except ValueError:
            print(f"[Attempt {attempts}/{MAX_ATTEMPTS}] Invalid input: please enter a numeric value (not letters or empty text).\n")
        except ZeroDivisionError:
            print(f"[Attempt {attempts}/{MAX_ATTEMPTS}] Cannot divide by zero: a campaign with 0 conversions has no cost per conversion.\n")
        else:
            print(f"Success! Cost per conversion: {cost_per_conversion:.2f} EUR")
            return

    print("Maximum attempts reached without a valid non-zero number. Exiting safely.")


if __name__ == "__main__":
    main()


# --- CHECK IT YOURSELF: Four test runs and observed behaviours ---
# 1. Normal number ("25"):
#    Converts cleanly to 25.0, computes 1200.0 / 25.0 = 48.00, prints "Success! Cost per conversion: 48.00 EUR", and exits cleanly.
# 2. Zero ("0"):
#    Converts to 0.0, triggers ZeroDivisionError on division, prints the specific zero-division message, and keeps running for the next attempt.
# 3. Word ("abc"):
#    Fails float("abc"), triggers ValueError, prints the specific non-numeric input message, and keeps running for the next attempt.
# 4. Empty line (""):
#    Strips to "", fails float(""), triggers ValueError, prints the specific non-numeric input message, and keeps running without crashing.
