def fib(num):
	fibonacciSequence = [0,1,1]
	for i in range(2, num):
		fibonacciSequence.append(fibonacciSequence[i] + fibonacciSequence[i - 1])
	return fibonacciSequence

fibonacciSequence = fib(61)
test_cases = int(input())
for _ in range(test_cases):
	index = int(input())
	print('Fib(%d) = %d'%(index, fibonacciSequence[index]))