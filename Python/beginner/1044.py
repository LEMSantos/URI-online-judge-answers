from sys import stdin, stdout
A, B = map(int, stdin.readline().split())
stdout.write(max(A, B) % min(A, B) and 'Nao sao Multiplos\n' or 'Sao Multiplos\n')