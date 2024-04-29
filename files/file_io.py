
import csv

companies = []
sales = []

with open("carSale.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        companies.append(row[0])
        sales.append([int(x.replace(',','')) for x in row[1:]])

# print(sales)

monthly_sales_sum = [sum(x) for x in zip(*sales)]
print("1.Sum of cars sold in each month")
print(monthly_sales_sum)
print("-" * 90)
yearly_sales_sum = {}
for i in range(len(companies)):
    yearly_sales_sum[companies[i]] = sum(sales[i])

print("2.Total yearly sales by each manufacturer")
for companies,sales in yearly_sales_sum.items():
    print(companies,sales)