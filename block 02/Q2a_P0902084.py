# TMA02 Question 2a: Program that checks whether a credit/debit card number is valid.

# Initialise a list containing the 16 digits of the card number
card_number = [4,9,6,9,9,0,4,7,1,2,3,4,2,0,8,4]

# Initialise the output list
checking_number = [0] * len(card_number)

# Initialise a variable for intermediate calculations
result = 0

# Apply the algorithm to each digit in the card number
for position in range(len(card_number)):

    # Modify the digits in odd-numbered positions
    if (position + 1) % 2 != 0:

        # Multiply the digit by 2 and store the result
        result = card_number[position] * 2

        # If the result is greater than 9, subtract 9 from the result
        if result > 9:
            result = result - 9

        # Append the result to the output list 
        checking_number[position] = result

    # Otherwise, append the digit unchanged to the output list
    else:
        checking_number[position] = card_number[position]

# Print the output list
print(checking_number)