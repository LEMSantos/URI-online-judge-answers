isOdd = lambda x: x % 2
x = int(input())
[print(i) for i in filter(isOdd, range(1, x + 1))]