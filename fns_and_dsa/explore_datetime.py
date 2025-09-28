from datetime import datetime, timedelta

def display_current_datetime():
    """
    Get current date and time, store it in current_date, and print it
    in the format YYYY-MM-DD HH:MM:SS.
    """
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(days):
    """
    Calculate future date by adding `days` to the current date.
    Save the result in future_date and print it as YYYY-MM-DD.
    """
    current_date = datetime.now()
    future_date = (current_date + timedelta(days=days)).date()
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    # Part 1: display current date/time
    display_current_datetime()

    # Part 2: prompt user and compute future date
    # NOTE: prompt text kept exactly as specified in the instructions/example.
    days_input = input("Enter the number of days to add to the current date: ")
    # Convert to int (assumes valid integer as stated in task)
    days = int(days_input)
    calculate_future_date(days)

if __name__ == "__main__":
    main()
