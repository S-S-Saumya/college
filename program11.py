#program to calculate income tax
r = 0.20
sd = 10000.0
dd = 3000.0
income = float(input('Enter the gross income'))
num = int(input('Enter the number of dependents'))
t_income = income - sd - dd * num #calculates the taxable income
tax = t_income * r #calculates the income tax
print ('The Income tax is Rs.'+str(tax))
