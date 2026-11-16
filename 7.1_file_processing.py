"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - There are completely blank lines (lines 3 and 9).
# - Some lines have leading whitespace before the first name ("  alan TURING", "  linus torvalds").
# - Capitalization is completely inconsistent across lines (all lowercase like "grace hopper",
#   UPPERCASE last name like "ada LOVELACE", or UPPERCASE first name like "GUIDO van rossum").
# - One entry has a multi-word last name ("GUIDO van rossum" has three words instead of two).
# - The names are not sorted alphabetically by last name.

# 1. In:
#    The raw text file "names.txt" containing 10 lines total (8 names and 2 blank lines).
# 2. Process, problem by problem:
#    - Leading/trailing spaces: stripped using .strip() on each line.
#    - Blank lines: skipped using "if line != ''" after stripping whitespace.
#    - Inconsistent capitalization: normalized to proper Title Case using .title().
#    - Multi-word last name ("Van Rossum"): handled by splitting on the first space only
#      (line.split(" ", 1)) so everything after the first name is kept together as the last name.
#    - Unsorted order: sorted alphabetically using a custom key that compares (last_name.lower(), first_name.lower()).
# 3. Out:
#    A new file named "cleaned_names.txt" containing the 8 cleaned, properly capitalized names
#    sorted alphabetically by last name (while leaving "names.txt" untouched).
# 4. How I decide which word is the last name:
#    Every line in this file follows the "FirstName LastName" order. Because "Guido Van Rossum"
#    has a two-word last name ("Van Rossum"), splitting on the first space only (split(" ", 1))
#    treats the first word as the first name and everything after the first space as the last name
#    (e.g., "Rossum" for "Guido Van Rossum", or the full surname "Van Rossum").


# Your code below
def get_sort_key(full_name):
    parts = full_name.split(" ", 1)
    first_name = parts[0].lower()
    last_name = parts[1].lower() if len(parts) > 1 else ""
    return (last_name, first_name)


def main():
    input_file = "names.txt"
    output_file = "cleaned_names.txt"

    cleaned_names = []

    with open(input_file, mode="r", encoding="utf-8") as infile:
        for raw_line in infile:
            stripped_line = raw_line.strip()
            if stripped_line == "":
                continue
            normalized_name = " ".join(stripped_line.split()).title()
            cleaned_names.append(normalized_name)

    sorted_names = sorted(cleaned_names, key=get_sort_key)

    with open(output_file, mode="w", encoding="utf-8") as outfile:
        for name in sorted_names:
            outfile.write(name + "\n")

    print(f"Done! {len(sorted_names)} cleaned names written to {output_file}.")


if __name__ == "__main__":
    main()
    