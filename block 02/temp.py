temperatures = [5, 4, 3, 2, -1, 0]
output_list = []

for temperature in temperatures:
    if temperature < 0 or temperature > 5:
        output_list = output_list + [temperature]

percentage =  (len(output_list) / len(temperatures)) * 100
print(int(percentage),'% of values are outside the range')
#print(f"{int(percentage)}% of the values are out of range")