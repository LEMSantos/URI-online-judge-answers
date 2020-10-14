def isTriangle(A, B, C):
    if (abs(B - C) < A < B + C) and \
    (abs(A - C) < B < A + C) and \
    (abs(A - B) < C < A + B):
    	return True
    return False

A, B, C = map(float, input().split())
if isTriangle(A, B, C):
    print('Perimetro = %.1f'%(A + B + C))
else:
    print('Area = %.1f'%(((A + B) * C) / 2))