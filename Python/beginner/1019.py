time = [3600,60,1]
value = int(input())
for index, t in enumerate(time):
	if index == 2:
		print('%d'%value)
		break
	print('%d'%(value // t),end=':')
	value %= t