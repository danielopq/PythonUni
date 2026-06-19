rate = 0.05
payment = 200
mortgage = 1000

print('Outstanding mortgage:',mortgage)
while(mortgage == 0 or mortgage < 0):
    interest = mortgage * rate / 12
    mortgage = mortgage + interest - payment
    print('Outstanding mortgage:',mortgage)
