# Check card number

# Initialise a list containing the 16 digits of the card number
card_number = [4,9,6,9,9,0,4,7,1,2,3,4,2,0,8,4]

# Initialise the output list
processed_digits = [0] * len(card_number)

# Initialise a variable for intermediate calculations
result = 0

# Initialise the aggregator to 0
aggregator = 0

# Apply the algorithm to each digit in the card number
for position in range(len(card_number)):

    # Modify the digits in odd-numbered positions
    if (position + 1) % 2 != 0:

        # Multiply the digit by 2 and store the result
        result = card_number[position] * 2

        # If the result is greater than 9, subtract 9 from the result
        if result > 9:
            result = result - 9

        # Store the result in the output list 
        processed_digits[position] = result

    # Otherwise, store the digit unchanged in the output list
    else:
        processed_digits[position] = card_number[position]

# Verify whether the transformed card number is valid

# Calculate the sum of the digits     
# For each digit in the list, Add the value of the digit to the aggregator
for digit in processed_digits:
    aggregator = aggregator + digit

# Find the remainder when the aggregator is divided by 10
reminder = aggregator % 10

# Check whether the number is valid
# If the remainder is not equal to the last digit, print ‘Number not valid'. Otherwise, print ‘The Number is valid.’
if reminder != processed_digits[len(processed_digits)-1]:
    print('Number not valid')
else:
    print('Number valid')