banknotes = [100,50,20,10,5,2]
bankcoins = [100,50,25,10,5,1]
value = float(input())
tmp_value = value
print('NOTAS:')
for note in banknotes:
	print('%d nota(s) de R$ %d.00'%(tmp_value // note, note))
	tmp_value %= note
print('MOEDAS:')
tmp_value = int(tmp_value * 100)
for coin in bankcoins:
	print('%d moeda(s) de R$ %.2f'%(tmp_value // coin, coin / 100))
	tmp_value %= coin