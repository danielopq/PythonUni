# Print right-angled triangle

size = 8

for line in range(0, size):
    for asterisk in range(0, size - line):
        print('*', end = '')
    print()