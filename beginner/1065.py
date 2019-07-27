isEven = lambda x: x % 2 == 0
even = list(filter(isEven, [int(input()) for _ in range(5)]))
print(len(even) ,'valores pares')