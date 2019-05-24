# Cross-matching GALEX catalog with GMRT catalog

import numpy as np
import math

# New file to store data
ofile = open('GALEX_large_match.txt', mode='w')

# Loading csv data into program references
galex = np.loadtxt('Large_GALEX_code.csv', delimiter=',')
gmrt = np.loadtxt('GMRT_400MHz_catalog_reduced.csv', delimiter=',')

# Linear Search Algorithm on NumPy Array
count = 1
count2 = 1
count3 = 0
flag = 0
innercount = 0
one = 0
two = 0
three = 0
four = 0    # Variables to note statistic distribution of data
five = 0
six = 0
seven = 0
eight = 0

for arr in gmrt:
    for arr1 in galex:
        d = math.sqrt(((arr[1]-arr1[1]) ** 2) + ((arr[3]-arr1[3]) ** 2))
        if d <= 10:
            print(arr)
            for z in range(0, 8):
                ofile.write(str(arr1[z]))
                ofile.write(" ")
            for a in range(0, 6):
                    ofile.write(str(arr[a]))
                    ofile.write(" ")
            ofile.write("\n")
            flag = 1
            innercount += 1
            print(f"GMRT:{count}, GALEX:{count2+1}")

        count2 += 1
    if innercount == 1:
        one += 1
    elif innercount == 2:
        two += 1
    elif innercount == 3:
        three += 1
    elif innercount == 4:
        four += 1
    elif innercount == 5:
        five += 1
    elif innercount == 6:
        six += 1
    elif innercount == 7:
        seven += 1
    elif innercount == 8:
        eight += 1
    if flag == 1:
        count3 += 1
    flag = 0
    count += 1
    count2 = 0
    innercount = 0

print(f"Total matching sources: {count3}")
print(f"One: {one} Two: {two} Three: {three} Four: {four} Five: {five} Six: {six} Seven: {seven} Eight: {eight}")
