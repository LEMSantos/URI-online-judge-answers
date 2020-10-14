parity = lambda x: x % 2 and 'ODD' or 'EVEN'
signal = lambda x: x > 0 and 'POSITIVE' or 'NEGATIVE'
test_cases = int(input())
for _ in range(test_cases):
	number = int(input())
	if number == 0:
		print('NULL')
	else:
		print(' '.join([parity(number), signal(number)]))