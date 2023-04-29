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
    sratecalc = usage + srate
    bill_amount = usage * wrate + sratecalc + sratebase
    return bill_amount

if __name__ == "__main__":
    print("Welcome to the Water Bill Calculator!")

    prev_reading = float(input("Enter your previous reading: "))
    new_reading = float(input("Enter your current reading: "))
    wrate = float(input("Enter your water cost per 1,000's: "))
    srate = float(input("Enter your sewer cost per 1,000's: "))
    sratebase = float(input("Enter your sewer cost base: "))
    

    bill_amount = calculate_water_bill(prev_reading, new_reading, wrate)
    print(f"Your water bill amount is: ${bill_amount:.2f}")
