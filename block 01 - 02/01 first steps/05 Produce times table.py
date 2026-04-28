# Produce times table

size = 12
for row in range (1, size + 1):
    for column in range (1, size +1):
        print (row * column)
        # move to new line
        print()
    print('-----------')