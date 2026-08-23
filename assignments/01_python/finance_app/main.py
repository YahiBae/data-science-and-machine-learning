from finance_tools.tax import calculate_tax
from finance_tools.loan import calculate_emi

income = float(input("Enter your income: "))
tax = calculate_tax(income)

print("Tax:", tax)

loan = float(input("Enter loan amount: "))
rate = float(input("Enter interest rate: "))
years = int(input("Enter loan years: "))

emi = calculate_emi(loan, rate, years)

print("Monthly EMI:", round(emi, 2))