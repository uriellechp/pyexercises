"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A Python dictionary defining a digital marketing campaign object with 5 key-value fields.
# 2. Process: Access a field, update a field value, safely attempt to access a non-existent field using .get(), remove a field with del, and iterate through all remaining key-value pairs.
# 3. Out: Specific field value, modified field value, safe fallback for missing field, and all key-value pairs printed line by line.
# 4. My object, my five fields, and why those:
#    - Object: A Digital Marketing Campaign.
#    - Fields:
#      * "campaign_name": Identifies the project (string).
#      * "channel": Marketing platform used (string).
#      * "monthly_budget": Allocated budget in euros (float).
#      * "is_active": Operational status of campaign (boolean).
#      * "target_country": Geographic scope for segmentation (string).

# Check it yourself results:
# - Accessing non-existent field using dict["non_existent"] raises KeyError and crashes the program.
# - Using dict.get("non_existent", "Not Found") safely returns "Not Found" without crashing.


# Your code below

# Dictionary describing a digital marketing campaign
campaign = {
    "campaign_name": "Summer Launch 2026",
    "channel": "Instagram Ads",
    "monthly_budget": 4500.00,
    "is_active": True,
    "target_country": "France"
}

# 1. Read one field
print("Campaign Name:", campaign["campaign_name"])

# 2. Change one field value
campaign["monthly_budget"] = 5200.00
print("Updated Budget:", campaign["monthly_budget"], "€")

# 3. Check it yourself: Safe access to a field that does not exist
missing_field = campaign.get("conversion_rate", "Field not available")
print("Missing field test:", missing_field)

# 4. Remove one field
del campaign["is_active"]

# 5. Display every remaining field with its value
print("\n--- Final Campaign Profile ---")
for key, value in campaign.items():
    print(f"{key}: {value}")
