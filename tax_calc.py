tax_employee

name=input('Enter empolyee name:')
employee_id=int(input('enter employee Id:'))
basic_monthly_salary=float(input('Enter basic monthly salary of the employee:'))
allowance=input('enter employee allowance:')
bonus_percentage=float(input('Enter employee bonus percentage:'))

gross_monthly_salary = basic_monthly_salary + allowance
annual_gross_salary = (gross_monthly_salary *12)+(gross_monthly_salary *(bonus_percentage / 100) * 12)

print(f'Employee name: {name}')
print(f'Employee ID: {Employee ID}')
print(f'Basic monthly salary: {Basic monthly salary}')
print(f'Employee monthly allowance: {Basic monthly salary}')
print(f'Gross monthly salary: {Gross monthly salary}')
print(f'Annual gross salary: {Annual gross salary}')

print('_' * 38)
print('%-25s :' % 'Employee name: {name}')
print('%-25s :' % 'Employee ID: {Employee ID}')
print('%-25s :' % 'Basic monthly salary: {Basic monthly salary}')
print('%-25s :' % 'Employee monthly allowance: {Basic monthly salary}')
print('%-25s :' % 'Gross monthly salary: {Gross monthly salary}')
print('%-25s :' % 'Annual gross salary: {Annual gross salary}')
print('_' * 38)