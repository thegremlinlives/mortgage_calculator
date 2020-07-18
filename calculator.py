def format_price(pence):
    return int(pence)/100.0

def print_formatted_price(prefix, pence):
    print(prefix, ' : ', format_price(pence))

def get_total_payments(debt, rate, months, monthly):
    total_rent_paid = 0
    total_debt_paid = 0
    remaining_debt = debt
    total_paid = 0
    for month in range(0, int(months)):
        rent_payment = remaining_debt*rate/1200
        total_rent_paid += rent_payment
        debt_payment = monthly - rent_payment
        total_debt_paid += debt_payment
        remaining_debt -= debt_payment

    return total_debt_paid, total_rent_paid


def calculate_monthly(debt, rate, months):
    increment = 100000
    monthly = increment
    previous_monthly = 0
    while increment > 0:
        debt_paid, rent_paid = get_total_payments(debt, rate, months, monthly)
        if debt_paid > debt:
            monthly -= increment
            increment = int(increment/10)
            if not increment:
                break
        elif debt_paid < debt:
            monthly += increment
        else:
            break
    return monthly + 1


debt = 20000000 # pence
years = 20
months = years*12
rate = 5

monthly = calculate_monthly(debt, rate, months)
debt_paid, rent_paid = get_total_payments(debt, rate, months/2.0, monthly)

print_formatted_price('monthly', monthly)
print_formatted_price('total debt paid', debt_paid)
print_formatted_price('total rent paid', rent_paid)
