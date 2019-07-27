salary = float(input()) - 2000.00
taxes = [(1000, 0.08), (1500, 0.18)]
taxes_sum = 0
for limit, taxe in taxes:
	taxes_sum += min(salary, limit) * taxe
	salary = max(0, salary - limit)
taxes_sum += salary * 0.28
if taxes_sum > 0:
	print('R$ %.2f'%taxes_sum)
else:
	print('Isento')