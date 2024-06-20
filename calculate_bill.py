def calculate_bill(units):
    # Define tariff rates
    tariff_slabs = [(0, 50, 3.00), (51, 100, 4.00), (101, 200, 5.50), (201, 300, 6.50), (301, 500, 7.50)]
    additional_charge = 0.10  # Additional charge for units above 500

    # Calculate bill based on units consumed
    total_bill = 0
    remaining_units = units

    for slab in tariff_slabs:
        start, end, rate = slab
        if remaining_units > 0:
            units_in_slab = min( remaining_units, end - start + 1 )
            total_bill += units_in_slab * rate
            remaining_units -= units_in_slab
        else:
            break

    # Add additional charge for units above 500
    if remaining_units > 0:
        total_bill += remaining_units * additional_charge

    return total_bill


def main():
    try:
        units = float( input( "Enter the number of units consumed: " ) )
        bill_amount = calculate_bill( units )
        print( "Electricity Bill: $", round( bill_amount, 2 ) )
    except ValueError:
        print( "Invalid input. Please enter a valid number of units." )


if name == "main":
    main()