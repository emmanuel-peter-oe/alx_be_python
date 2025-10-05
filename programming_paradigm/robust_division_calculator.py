def safe_divide(numerator, denominator):
    try:
        # Convert to float
        num = float(numerator)
        den = float(denominator)

        # Handle divide by zero
        if den == 0:
            return "Error: Cannot divide by zero."

        # Return result
        result = num / den
        return f"The result of the division is {result:.1f}"

    except ValueError:
        # Non-numeric input
        return "Error: Please enter numeric values only."
