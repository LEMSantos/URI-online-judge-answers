isPositive = lambda x: x >= 0
positive = list(filter(isPositive, [float(input()) for _ in range(6)]))
print(len(positive) ,'valores positivos')
print('%.1f'%(sum(positive) / len(positive)))