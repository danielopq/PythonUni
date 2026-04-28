# Print right-angled triangle

size = 3

for line in range(1, size + 1):
    for asterisk in range(1, line + 1):
        print('*', end = '')
    print()