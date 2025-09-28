# temp_conversion_tool.py

# Global conversion factors (exactly as required by the checker)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt user for temperature
        temp = float(input("Enter the temperature to convert: "))
        
        # Prompt for unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == "F":
            # Convert F -> C
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result}°C")
        elif unit == "C":
            # Convert C -> F
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result}°F")
        else:
            # Invalid unit
            raise ValueError("Invalid temperature. Please enter a numeric value.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
