# Task 1

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

week_2_temps = temperatures[7:14]

print(week_2_temps)

# Task 2

high_temps = temperatures[temperatures.index(100):]

print(high_temps)

# Task 3

temperatures.reverse()
print(temperatures[4:10])