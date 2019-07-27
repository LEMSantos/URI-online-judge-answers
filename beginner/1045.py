functions = [lambda A, B, C: A >= B + C,
			 lambda A, B, C: A**2 == B**2 + C**2,
			 lambda A, B, C: A**2 > B**2 + C**2,
			 lambda A, B, C: A**2 < B**2 + C**2,
			 lambda A, B, C: bool(A == B and B == C),
			 lambda A, B, C: (A == B and A != C) or (B == C and B != A) or (A == C and A != B)]

message = ['NAO FORMA TRIANGULO', 'TRIANGULO RETANGULO', 'TRIANGULO OBTUSANGULO',
		   'TRIANGULO ACUTANGULO', 'TRIANGULO EQUILATERO', 'TRIANGULO ISOSCELES']

A, B, C = sorted(map(float, input().split()), reverse=True)
triangles = [func(A, B, C) for func in functions]
if triangles[0]:
	print(message[0])
else:
	[print(msg) for i, msg in enumerate(message) if triangles[i]]