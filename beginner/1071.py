x = int(input())
y = int(input())
result = sum(filter(lambda x: x % 2, range(min(x,y) + 1, max(x,y))))
print(result)