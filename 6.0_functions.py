# 1. In: A list of numbers representing daily sales amounts in euros (sales).
# 2. Process: It checks if the list is empty to avoid dividing by zero; otherwise,
#    it sums all the sales and divides the total by the number of elements in the list.
# 3. Out: A single float representing the average sale amount (or 0.0 if the list is empty).
# 4. My function name, and why return rather than print:
#    The function is called "calculate_average_sale". Its name clearly states what it
#    computes and on what kind of data without needing to read the body of the function.
#    Using "return" instead of "print" is essential because "print" only displays text
#    on the screen and evaluates to None, whereas "return" sends the actual computed
#    value back to the caller so it can be stored in a variable, reused in further
#    calculations, or saved to a file.


# Your code below
def calculate_average_sale(sales):
    if len(sales) == 0:
        return 0.0
    return sum(sales) / len(sales)


# Three calls with different inputs
week_1_sales = [120.5, 85.0, 210.0, 145.5]
week_2_sales = [50.0, 60.0, 70.0]
week_3_sales = [310.0, 490.0, 250.0, 350.0, 400.0]

avg_1 = calculate_average_sale(week_1_sales)
avg_2 = calculate_average_sale(week_2_sales)
avg_3 = calculate_average_sale(week_3_sales)

print(f"Week 1 average sale: {avg_1:.2f} EUR")
print(f"Week 2 average sale: {avg_2:.2f} EUR")
print(f"Week 3 average sale: {avg_3:.2f} EUR")

# Empty list check
empty_avg = calculate_average_sale([])
print(f"Empty list average sale: {empty_avg:.2f} EUR")
# Comment on empty list behaviour:
# Without a check, dividing by len(sales) on an empty list raises a ZeroDivisionError
# and crashes the program. With the "if len(sales) == 0" guard, it returns 0.0 instead.
# This behaviour is acceptable because it prevents crashes when no sales data is recorded yet.
