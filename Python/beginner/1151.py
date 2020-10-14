def fast_fib_generator(num):
	F = [1, 1]
	yield 0
	yield 1
	yield 1
	for k in range(1, num):
		F.append(F[k] ** 2 + F[k - 1] ** 2)
		yield F[-1]
		F.append(F[k] * (2 * F[k + 1] - F[k]))
		yield F[-1]

fibSeq = fast_fib_generator(23)
num = int(input())
for index, i in enumerate(fibSeq):
	if index == num - 1:
		print(i)
		break
	print(i ,end = ' ')