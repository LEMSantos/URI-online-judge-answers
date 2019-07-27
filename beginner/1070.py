x = int(input())
odd = x % 2 and x or x + 1
[print(x) for x in range(odd, x + 12, 2)]