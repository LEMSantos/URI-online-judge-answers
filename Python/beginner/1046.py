begin, end = map(int, input().split())
if end > begin:
	time = end - begin
else:
	time = 24 - begin + end
print('O JOGO DUROU %d HORA(S)'%time)