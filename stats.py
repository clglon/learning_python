#!/usr/bin/env python3

from math import sqrt
import fileinput

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!

data = []
for line in fileinput.input():
	if line.startswith('#'): continue # same as above
	line = line.rstrip() # remove newline (return character), often useful
	data.append(float(line)) # store the data



# to count the total number of values in data list
count = 0
for num in data:
    count += 1
print("Count:", count)

print("Minimum:", min(data)) # prints the minimum value
print("Maximum:", max(data)) # prints the maximum value

# calculates the mean of the data list
mean = sum(data)/count
print("Mean:", mean)

'''
How to calculate Standard Deviation
1. Work out the Mean (the simple average of the numbers)
2. Then for each number: subtract the Mean and square the result.
3. Then work out the mean of those squared differences.
4. Take the square root of that and we are done!
'''
# caclulates the standard deviation of the data list
sd_data = [] # create a new list to hold the number - mean value
for num in data:
    temp = (num - mean)**2
    sd_data.append(float(temp)) # adds value to new list
sd_mean = sqrt(sum(sd_data)/count) # takes the average of the list and squares the result
# format std dev to only 3 decimal places
sd_mean_formatted = '{:.3f}'.format(sd_mean)
print("Std. dev:", sd_mean_formatted)

# find the median value of the data list
# sort the list and then average the two middle values since even nubmer list?
sorted_data = sorted(data)

# method 1 - blunt, direct, not universal
median_sum = (sorted_data[4] + sorted_data[5])/2
print(median_sum)

# method 2 - ability to calculate the median if more values are added to list
if count%2 == 0:
    left = int(count/2 - 1)
    right = int(count/2)
    median_sum = (sorted_data[left] + sorted_data[right])/2
    print(median_sum)
else:
    middle = int((count/2) + 0.5)
    print = sorted_data[middle]


"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
