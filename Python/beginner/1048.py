increanse = [(0, 400, 1.15), (400.01, 800, 1.12), (800.01, 1200, 1.1),
			(1200.01, 2000.00, 1.07)]
			
salary = float(input())
new_salary = [(salary * inc, (inc - 1)*100) for ini, end, inc in increanse if ini <= salary <= end]
new_salary, inc = new_salary and new_salary[0] or (salary * 1.04, 4.0)
print('Novo salario: %.2f'%new_salary)
print('Reajuste ganho: %.2f'%(new_salary - salary))
print('Em percentual: %d %%'%(int(round(inc, 2))))