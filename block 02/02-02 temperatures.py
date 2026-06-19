daily_temperatures = [28,33,29,32,27]
hot_days = []

for temperature in daily_temperatures:
    if temperature > 30:
        hot_days = hot_days +[temperature]

print('The hot days had tempratures',hot_days)