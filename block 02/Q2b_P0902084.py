# Verify whether the transformed card number is valid

# Initialise the input list with the transformed card number
processed_digits = [8, 9, 3, 9, 9, 0, 8, 7, 2, 2, 6, 4, 4, 0, 7, 4]

# Initialise the aggregator to 0
aggregator = 0

# Calculate the sum of the digits     
# For each digit in the list, Add the value of the digit to the aggregator
for digit in processed_digits:
    aggregator = aggregator + digit

# Find the remainder when the aggregator is divided by 10
reminder = aggregator % 10

# Check whether the number is valid
# If the remainder is not equal to the last digit, print ‘Number not valid'. Otherwise, print ‘Number valid’
if reminder != processed_digits[len(processed_digits)-1]:
    print('Number not valid')
else:
    print('Number valid')
