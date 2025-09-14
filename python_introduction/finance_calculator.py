# Prompt the user for financial details
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Project annual savings with 5% interest
annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Display results
print("Your monthly savings are $", monthly_savings)
print("Projected savings after one year, with interest, is: $", annual_savings)