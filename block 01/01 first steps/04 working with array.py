# Working with arrays

amounts = [1, 4, 8, 10]
total = 0
# Print all the amounts

for index in range (0, len(amounts)):
    print(amounts[index])
    total = total + amounts[index]

print(total)
