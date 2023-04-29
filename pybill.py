def calculate_water_bill(prev_reading, new_reading, rate):
    """
    Calculates the water bill based on previous and new readings and a rate per unit.

    Args:
    prev_reading (float): The previous water meter reading.
    new_reading (float): The new water meter reading.
    rate (float): The rate per unit of water consumed.

    Returns:
    float: The calculated water bill amount.
    """
    usage = new_reading - prev_reading
    bill_amount = usage * rate
    return bill_amount

if __name__ == "__main__":
    print("Welcome to the Water Bill Calculator!")

    prev_reading = float(input("Enter your previous reading: "))
    new_reading = float(input("Enter your current reading: "))
    rate = float(input("Enter the rate per unit: "))
    print("Commonly measured in 1,000 of Gallons)")

    bill_amount = calculate_water_bill(prev_reading, new_reading, rate)
    print(f"Your water bill amount is: ${bill_amount:.2f}")
