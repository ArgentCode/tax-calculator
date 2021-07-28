# income tax rates
# 10%: up to 9950
# 12%: 9950 to 40525
# 22%: 40526 to 86375
# 24%: 86375+

def income_tax(taxable_income):
    first = 9950 *0.9
    second = 40525*0.88
    third = 86375*0.78
    if taxable_income > 86375:
        fourth = (taxable_income - 86375)*0.76
        return fourth+third+second+first

    if taxable_income > 40525:
        third = (taxable_income - 86375)*0.78
        return third+second+first

    if taxable_income > 9950:
        second = (taxable_income - 86375) * 0.78
        return second + first

    return taxable_income*0.9


if __name__ == '__main__':
    taxable_income = 5000
    print(income_tax(taxable_income))
