x = int(input())
for i in range(1, x + 1):
	quad, cub = pow(i, 2), pow(i, 3)
	print(i, quad, cub)
	print(i, quad + 1, cub + 1)