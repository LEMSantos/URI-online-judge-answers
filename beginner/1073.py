isEven = lambda x: x % 2 == 0
N = int(input())
[print('%d^2 = %d'%(i, i**2)) for i in filter(isEven, range(1, N + 1))]