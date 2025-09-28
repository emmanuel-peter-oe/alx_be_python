# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global FAHRENHEIT_TO_CELSIUS_FACTOR.
    """
    # uses the global factor (read-only)
    return (fahrenheit - 32.0) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global CELSIUS_TO_FAHRENHEIT_FACTOR.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32.0

def main():
    # Prompt for temperature (must be numeric)
    temp_str = input("Enter the temperature to convert: ").strip()
    try:
        temp_value = float(temp_str)
    except Exception:
        # As required by the task: raise an error with this exact message
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Prompt for unit (C or F)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        result_c = convert_to_celsius(temp_value)
        # Print with raw float (example output shows full precision)
        print(f"{temp_value}°F is {result_c}°C")
    elif unit == "C":
        result_f = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {result_f}°F")
    else:
        # invalid unit: print helpful message (not specified to raise)
        print("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
