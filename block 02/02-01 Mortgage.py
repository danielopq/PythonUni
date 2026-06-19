rate = 0.05
payment = 200
mortgage = 1000
outstanding = []

outstanding = outstanding + [mortgage]

while(mortgage > 0):
    interest = mortgage * rate / 12
    mortgage = mortgage + interest - payment
    outstanding = outstanding + [mortgage]

print('Outstanding mortgage, month by month:',outstanding)
