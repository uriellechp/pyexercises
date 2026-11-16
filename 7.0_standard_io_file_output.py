"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In:
#    Four inputs typed by the user in the terminal:
#    - item_name (string, non-empty)
#    - platform (string, must be one of: Vinted, Depop, Vestiaire, Other)
#    - cost_eur (float, must be >= 0)
#    - sold_price_eur (float, must be >= 0)
# 2. Process:
#    - Each input is validated in a loop so invalid entries (empty text, unknown platform,
#      negative numbers, or non-numeric prices) are rejected and re-asked until valid.
#    - Commas inside text inputs are replaced with spaces to avoid breaking CSV columns.
#    - The program computes net profit (sold_price_eur - cost_eur).
#    - It checks if "sales_tracker.csv" already exists (or is empty). If not, it creates the file
#      and writes the header row first; otherwise, it opens it in append mode ("a") and adds
#      only the new data row without repeating the header.
# 3. Out, file name and columns:
#    - File name: sales_tracker.csv
#    - Columns: item_name,platform,cost_eur,sold_price_eur,profit_eur
# 4. Why these columns, and what this file is for:
#    I chose these five columns to track secondhand fashion resale transactions (item name,
#    selling platform, sourcing cost, final sale price, and calculated net profit).
#    Once this file has 200 rows, I would analyze which platform generates the highest average
#    profit margin, identify which types of clothing sell best, and spot any items sold at a loss.


# Your code below
import os


def get_non_empty_text(prompt):
    while True:
        value = input(prompt).strip().replace(",", " ")
        if value != "":
            return value
        print("Invalid input: text cannot be empty. Please try again.")


def get_valid_platform(prompt):
    valid_platforms = ["Vinted", "Depop", "Vestiaire", "Other"]
    while True:
        value = input(prompt).strip().capitalize()
        if value in valid_platforms:
            return value
        print(f"Invalid platform. Choose one of: {', '.join(valid_platforms)}.")


def get_non_negative_float(prompt):
    while True:
        raw_value = input(prompt).strip().replace(",", ".")
        try:
            number = float(raw_value)
            if number >= 0:
                return number
            print("Invalid amount: price cannot be negative.")
        except ValueError:
            print("Invalid amount: please enter a valid number (e.g., 25.50).")


def main():
    file_name = "sales_tracker.csv"
    header = "item_name,platform,cost_eur,sold_price_eur,profit_eur\n"

    print("--- Record a New Sale ---")
    item_name = get_non_empty_text("Item name: ")
    platform = get_valid_platform("Platform (Vinted / Depop / Vestiaire / Other): ")
    cost_eur = get_non_negative_float("Purchase cost (EUR): ")
    sold_price_eur = get_non_negative_float("Sold price (EUR): ")
    profit_eur = round(sold_price_eur - cost_eur, 2)

    file_needs_header = not os.path.exists(file_name) or os.path.getsize(file_name) == 0

    with open(file_name, mode="a", encoding="utf-8") as csv_file:
        if file_needs_header:
            csv_file.write(header)
        row = f"{item_name},{platform},{cost_eur:.2f},{sold_price_eur:.2f},{profit_eur:.2f}\n"
        csv_file.write(row)

    print(f"Saved to {file_name}! Net profit: {profit_eur:.2f} EUR")


if __name__ == "__main__":
    main()