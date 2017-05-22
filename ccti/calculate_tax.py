slabs = [(0, 1000, 15), (1000, 5000, 20), (5000, 7500, 25), (7500, None, 40)]

income = 10000
remaining_income = 10000
total_tax = 0

for slab in slabs:
    lower_bound = slab[0]
    upper_bound = slab[1]
    tax_percent = slab[2]

    if upper_bound:
        if income > upper_bound:
            remaining_income = income - upper_bound
            taxable_sal = upper_bound - lower_bound
        else:
            taxable_sal = remaining_income
            remaining_income = upper_bound - remaining_income
            upper_bound = None
    else:
        taxable_sal = remaining_income

    tax = (taxable_sal * tax_percent)/100
    total_tax += tax

    if not upper_bound:
        print total_tax
        break