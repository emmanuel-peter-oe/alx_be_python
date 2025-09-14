# 1) Read input (explicit variable names checker expects)
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# 2) Monthly savings
monthly_savings = monthly_income - monthly_expenses

# 3) Projected savings after one year with 5% interest
savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Helper to print clean integers when possible (matches example output)
def fmt_amount(x):
    x = float(x)
    return str(int(x)) if x.is_integer() else f"{x:.2f}"

# 4) Output in the expected format
print("Your monthly savings are $" + fmt_amount(monthly_savings) + ".")
print("Projected savings after one year, with interest, is: $" + fmt_amount(savings) + ".")