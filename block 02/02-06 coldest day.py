temperatures = [5,0,-1,18,12,-6,35,0,1]
coldest = temperatures[0]

for temperature in temperatures:
    if temperature < coldest:
        coldest = temperature

print('The lowest temperature of',temperatures,'is',coldest)