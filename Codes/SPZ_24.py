# Cross-matching SPITZER SWIRE 24 micron catalog with GMRT catalog

import numpy as np
import math

# New file to store data
ofile = open('SPITZER_24_match4.txt', mode='w')

# Loading csv data into program references
spitzer = np.loadtxt('CSV_Files/SPITZER_24_reduced.csv', delimiter=',')
gmrt = np.loadtxt('CSV_Files/GMRT_400MHz_catalog_reduced.csv', delimiter=',')

# Linear Search Algorithm on NumPy Array
count = 1
count2 = 1
count3 = 0
flag = 0

for arr in gmrt:
    for arr1 in spitzer:
        d = math.sqrt(((arr[1] - arr1[1]) ** 2) + ((arr[3] - arr1[3]) ** 2))
        if d <= 5:
            print(arr)
            for z in range(0, 6):
                ofile.write(str(arr1[z]))
                ofile.write(" ")
            for a in range(0, 6):
                    ofile.write(str(arr[a]))
                    ofile.write(" ")
            ofile.write("\n")
            flag = 1
            print(f"GMRT:{count}, SPITZER:{count2+1}")

        count2 += 1
    if flag == 1:
        ofile.write("\n")
        count3 += 1

    flag = 0
    count += 1
    count2 = 0

print(f"Total number of matching sources: {count3}")
