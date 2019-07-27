numbers = int(input())
count = 0
inInterval = lambda x: (10 <= x <= 20) and True or False
for _ in range(numbers):
	if inInterval(int(input())):
		count += 1

print(count, 'in')
print(numbers - count, 'out')