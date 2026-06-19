celsius_values = [28,33,29,32,27]
farenheit_values = []

for celsius in celsius_values:
    farenheit = celsius * 1.8 + 32
    farenheit_values = farenheit_values + [farenheit]
print('The temperatures in Fahrenheit are',farenheit_values)