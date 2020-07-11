import numpy as np

# New file to store Master Catalog
ofile = open('Master_Catalog.txt', mode='w')

# Opening all the catalogs to be merged
gmrt = np.loadtxt('CSV_Files/GMRT_400MHz_unq.csv', delimiter=',')
galex = np.loadtxt('CSV_Files/GALEX_unq_large.csv', delimiter=',')
spz24 = np.loadtxt('CSV_Files/SPITZER_24_unq.csv', delimiter=',')
spz70 = np.loadtxt('CSV_Files/SPITZER_70_unq.csv', delimiter=',')
spz160 = np.loadtxt('CSV_Files/SPITZER_160_unq.csv', delimiter=',')
spz05 = np.loadtxt('CSV_Files/SPITZER_s05_unq.csv', delimiter=',')
servs1 = np.loadtxt('CSV_Files/SPITZER_servs1_unq.csv', delimiter=',')
servs2 = np.loadtxt('CSV_Files/SPITZER_servs2_unq.csv', delimiter=',')
servs12 = np.loadtxt('CSV_Files/SPITZER_servs12_unq.csv', delimiter=',')

flag = 0

for arr in gmrt:

    for x in range(0, 4):
        ofile.write(str(arr[x]))
        ofile.write(" ")

    for arr1 in galex:
        if arr1[0] == arr[0] and arr1[1] == arr[1]:
            flag = 1
            for x in range(2, 6):
                ofile.write(str(arr1[x]))
                ofile.write(" ")
            break
    if flag == 0:
        for x in range(2, 6):
            ofile.write('0')
            ofile.write(" ")

    flag = 0

    for arr2 in spz24:
        if arr2[0] == arr[0] and arr2[1] == arr[1]:
            flag = 1
            for x in range(2, 4):
                ofile.write(str(arr2[x]))
                ofile.write(" ")
            break
    if flag == 0:
        for x in range(2, 4):
            ofile.write('0')
            ofile.write(" ")

    flag = 0

    for arr3 in spz70:
        if arr3[0] == arr[0] and arr3[1] == arr[1]:
            flag = 1
            for x in range(2, 4):
                ofile.write(str(arr3[x]))
                ofile.write(" ")
            break
    if flag == 0:
        for x in range(2, 4):
            ofile.write('0')
            ofile.write(" ")

    flag = 0

    for arr4 in spz160:
        if arr4[0] == arr[0] and arr4[1] == arr[1]:
            flag = 1
            for x in range(2, 4):
                ofile.write(str(arr4[x]))
                ofile.write(" ")
            break
    if flag == 0:
        for x in range(2, 4):
            ofile.write('0')
            ofile.write(" ")

    flag = 0

    for arr5 in spz05:
        if arr5[0] == arr[0] and arr5[1] == arr[1]:
            flag = 1
            for x in range(2, 12):
                ofile.write(str(arr5[x]))
                ofile.write(" ")
            break
    if flag == 0:
        for x in range(2, 12):
            ofile.write('0')
            ofile.write(" ")

    flag = 0

    for arr6 in servs1:
        if arr6[0] == arr[0] and arr6[1] == arr[1]:
            flag = 1
            for x in range(2, 15):
                ofile.write(str(arr6[x]))
                ofile.write(" ")
            break
    if flag == 0:
        for x in range(2, 15):
            ofile.write('0')
            ofile.write(" ")

    flag = 0

    for arr7 in servs2:
        if arr7[0] == arr[0] and arr7[1] == arr[1]:
            flag = 1
            for x in range(2, 15):
                ofile.write(str(arr7[x]))
                ofile.write(" ")
            break
    if flag == 0:
        for x in range(2, 15):
            ofile.write('0')
            ofile.write(" ")

    flag = 0

    for arr8 in servs12:
        if arr8[0] == arr[0] and arr8[1] == arr[1]:
            flag = 1
            for x in range(2, 28):
                ofile.write(str(arr8[x]))
                ofile.write(" ")
            break
    if flag == 0:
        for x in range(2, 28):
            ofile.write('0')
            ofile.write(" ")

    flag = 0
    ofile.write("\n")

print("Master Catalog successfully generated!")








