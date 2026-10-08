"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: User confirmations typed as strings in response to a campaign budget approval prompt.
# 2. Process: Prompt the user repeatedly up to a maximum limit (3 attempts), cleaning inputs with .strip().lower(). Loop stops when user types "yes" or reaches 3 attempts.
# 3. Out: A summary indicating whether budget approval succeeded or failed, along with the total number of attempts made.
# 4. My stop condition, my attempt limit, my summary:
#    - Stop condition: User answers "yes" (handles extra spaces and uppercase via .strip().lower()).
#    - Attempt limit: Maximum 3 attempts to prevent infinite loops.
#    - Summary: Displays total attempts used and whether campaign budget was approved or rejected due to maximum attempts reached.

# Check it yourself results:
# - Tested with wrong answers 3 times ("no", "maybe", "invalid"): Program stopped after 3 attempts with failure summary.
# - Tested with extra spaces/capitals ("  YES  "): Cleanly accepted on attempt 1 with success summary.


# Your code below

max_attempts = 3
attempts = 0
approved = False

while attempts < max_attempts and not approved:
    attempts += 1
    user_response = input(f"Attempt {attempts}/{max_attempts} — Approve campaign budget? (yes/no): ")
    
    # Cleaning input: remove surrounding spaces and convert to lowercase
    cleaned_response = user_response.strip().lower()
    
    if cleaned_response == "yes":
        approved = True
    else:
        print("Invalid or negative answer. Please try again.")

# Final summary display
print("\n--- Summary ---")
print(f"Total attempts made: {attempts}")
if approved:
    print("Status: Campaign budget approved successfully.")
else:
    print("Status: Operation failed. Maximum number of attempts reached.")