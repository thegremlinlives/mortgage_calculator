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

    return round(total_debt_paid, 2), round(total_rent_paid, 2)


def calculate_monthly(debt, rate, months):
    begin = 0
    end = debt
    while 1:
        monthly = round((begin + end)/2.0, 2)
        debt_paid, rent_paid = get_total_payments(debt, rate, months, monthly)
        if debt_paid > debt:
            if end == monthly:
                break
            end = monthly
        elif debt_paid < debt:
            if begin == monthly:
                monthly += 0.01
                break
            begin = monthly
        else:
            break
    return monthly


debt = 200000 # + 38000
years = 20
months = years*12
rate = 8

monthly = calculate_monthly(debt, rate, months)
debt_paid, rent_paid = get_total_payments(debt, rate, 10*12, monthly)

print('monthly : ', monthly)
print('total debt paid : ', debt_paid)
print('total rent paid : ', rent_paid)
print('total cost : ', debt_paid + rent_paid)
