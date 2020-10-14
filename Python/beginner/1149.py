from sys import stdin, stdout 
numbers = tuple(map(int, stdin.readline().split()))
summation = sum(range(numbers[0],numbers[0] + numbers[-1])) 
stdout.write('%s\n'%str(summation))