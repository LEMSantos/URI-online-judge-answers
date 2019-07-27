time_days = int(input())
years = time_days // 365
months = (time_days - years * 365) // 30
days = time_days - months * 30 - years * 365
print('%d ano(s)'%years)
print('%d mes(es)'%months)
print('%d dia(s)'%days)