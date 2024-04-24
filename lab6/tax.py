# Instructions
# The rules for simple tax calculation is as follows:
#     Personal allowance:		£11,850
#       0 to 34,500 			taxed at 20%
#       34,501 to 150,000 		taxed at 40%
#       Over 150,000 			taxed at 45%

def getIncomeTax(salary):

    personal_allowance = 11850
    taxable_income = salary - personal_allowance

    print("Salary Breakdown for Yearly Salary £{salary_value:,} :-".format(salary_value=salary))
    print("Yearly Personal Allowance : £{personal_allowance_value:,}".format(personal_allowance_value=personal_allowance))

    if 0 <= taxable_income <= 34500:
        income_tax_percent = 20
    elif 34501 <= taxable_income <= 150000:
        income_tax_percent = 40
    elif taxable_income > 150000:
        income_tax_percent = 45
    else:
        income_tax_percent = 0

    if income_tax_percent > 0:
        income_tax = (taxable_income * income_tax_percent)/100
    else:
        income_tax = 0

    take_home_salary = taxable_income - income_tax

    print("Yearly Taxable Income : £{taxable_income_value:,}".format(taxable_income_value=taxable_income))
    print("Yearly Income Tax  @ {income_tax_percent_value}% : £{income_tax_value:,.2f}"
          .format(income_tax_percent_value=income_tax_percent , income_tax_value=income_tax))
    print("Yearly Take Home Income : £{take_home_salary_value:,.2f}".format(take_home_salary_value=take_home_salary))


salary_input = int(input("Please enter your yearly salary in £"))

getIncomeTax(salary_input)

