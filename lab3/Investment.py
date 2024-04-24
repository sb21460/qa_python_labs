# assuming the interest is simple interest
# Final Amount =  Initial Principle ( 1 + Annual rate of interest * time in years)

initial_investment = float(input("Please enter Initial Investment in £: "))
target_value = float(input("Please enter Target Value in £: "))
interest_rate = float(input("Please enter simple interest % rate per year: "))

time_in_years = ((target_value / initial_investment) - 1) * 100 / interest_rate

print(f"£{initial_investment} will become £{target_value} in {time_in_years}years with "
      f"{interest_rate}% simple interest rate.")
