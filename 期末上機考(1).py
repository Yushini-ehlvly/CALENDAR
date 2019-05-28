import numpy as np
arrMonth = np.array(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])

year = int(input("Enter the year(2018):"))
while year != 2018:
    print("Enter error")
    year = int(input ("Enter the year(2018):"))
    
for n in range(0, 12):
    i = 1900
    sum = 0
    while i < year - 1:
        i += 1
        if((i % 4 == 0 and i % 100 != 0) or (i % 400 == 0)):sum += 366
        else: sum += 365
    month = n + 1
    j = 1
    while j < month:
        if((j == 1) or (j == 3) or (j == 5) or (j == 7) or (j == 8) or (j == 10) or (j == 12)):sum += 31
        elif j == 2:
            sum += 28
        else: sum += 30
        j += 1
    week = (sum + 1) % 7
    if ((month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12)):day = 31
    elif month == 2:
        day = 28
    else:day = 30
    print(arrMonth[n])
    print("Sun\tMon\tTue\tWed\tThr\tFri\tSat")
    count = 0
    k = 0
    while k <= week:
        k += 1
        print("\t",end="")
        count += 1
        if (count % 7 == 0):
            print("\n")
    p = 1
    while p <= day:
        print(p,"\t",end="")
        p += 1
        count += 1
        if(count % 7 == 0):
            print("\n")
    print()