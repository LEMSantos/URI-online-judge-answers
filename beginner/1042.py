def printValues(values):
    for value in values:
        print(value)
        
values = input().split()
printValues(sorted(values, key=int))
print()
printValues(values)