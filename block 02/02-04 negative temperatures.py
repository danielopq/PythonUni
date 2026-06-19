temperatures = [2,12,-8,-2,0,10,8,-1,10,18,21,12]
days=0

for temperature in temperatures:
    if temperature < 0:
        days = days + 1
print('The temperature was below 0 for',days,'days')