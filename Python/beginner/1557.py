while True:
	number = int(input())
	if not number:
		break
	formatStr = '%%%dd'%(len(str(2**(2*number - 2))))
	for i in range(number):
		for j in range(i, i + number):
			print(formatStr % (2**j), end='')
			if j == (i + number - 1):
				print()
			else:
				print(' ', end='')
	print()