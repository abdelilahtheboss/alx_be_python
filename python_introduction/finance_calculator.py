monthly_income = int(input('Enter your monthly income:  '))
monthly_expenses = int(input('Enter your total monthly expenses:  '))
monthly_savings = monthly_income - monthly_expenses
simple_annual_interest_rate = 0.05
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * simple_annual_interest_rate)
print('Your monthly savings are $'+str(monthly_savings)+ '.')
print('Projected savings after one year, with interest, is: $'+str(Projected_Savings)+ '.')