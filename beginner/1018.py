banknotes = [100,50,20,10,5,2,1]
value = int(input())
tmp_value = value
print(value)
for note in banknotes:
	print('%d nota(s) de R$ %d,00'%(tmp_value // note, note))
	tmp_value %= note