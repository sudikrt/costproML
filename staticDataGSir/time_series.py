import pandas as pd
import numpy as np
from random import randint

f = open ("outDataSingle.csv", "w+")

def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1
            else:
                m2 = x
    return m2 if count >= 2 else None

job = "Engineer"
min_sal = 500
max_sal = 1200
for index in range (2000, 2017) :
    for mon in range (1, 13):
        if mon == 2 :
            if index % 4 != 0 :
                mn = 1
                mx = 29
            else :
                mn = 1
                mx = 30
        else:
            if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
                mn = 1
                mx = 32
            else :
                mn = 1
                mx = 31
        for j in range (mn, mx) :
            a = []
            for i in range (1, 10) :
                a.append (randint(min_sal, max_sal))
                if index % 2 == 0:
                    large = second_largest(a)
                else:
                    large = max(a)
            if mon == 3 or mon == 5 :
                factor = 0.2
            elif mon == 7 or mon == 8 :
                factor = 0.3
            else :
                factor = 0.45
            large = int (large - large * factor)
            small = int (min (a) - min(a) * factor)
            f.write(job + ',' + str(str(index) + '-' + str(mon) + '-'+str(j)) + ',' + str (large) + ',' + str(small) +'\n')

job = "Tester"
min_sal = 400
max_sal = 900
for index in range (2000, 2017) :
    for mon in range (1, 13):
        if mon == 2 :
            if index % 4 != 0 :
                mn = 1
                mx = 29
            else :
                mn = 1
                mx = 30
        else:
            if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
                mn = 1
                mx = 32
            else :
                mn = 1
                mx = 31
        for j in range (mn, mx) :
            a = []
            for i in range (1, 10) :
                a.append (randint(min_sal, max_sal))
                if index % 2 == 0:
                    large = second_largest(a)
                else:
                    large = max(a)
            f.write(job + ',' + str(str(index) + '-' + str(mon) + '-'+str(j)) + ',' + str (large) + ',' + str(min (a)) +'\n')

job = "Carpenter"
min_sal = 350
max_sal = 700
for index in range (2000, 2017) :
    for mon in range (1, 13):
        if mon == 2 :
            if index % 4 != 0 :
                mn = 1
                mx = 29
            else :
                mn = 1
                mx = 30
        else:
            if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
                mn = 1
                mx = 32
            else :
                mn = 1
                mx = 31
        for j in range (mn, mx) :
            a = []
            for i in range (1, 10) :
                a.append (randint(min_sal, max_sal))
                if index % 2 == 0:
                    large = second_largest(a)
                else:
                    large = max(a)
            f.write(job + ',' + str(str(index) + '-' + str(mon) + '-'+str(j)) + ',' + str (large) + ',' + str(min (a)) +'\n')

job = "Cook"
min_sal = 400
max_sal = 800
for index in range (2000, 2017) :
    for mon in range (1, 13):
        if mon == 2 :
            if index % 4 != 0 :
                mn = 1
                mx = 29
            else :
                mn = 1
                mx = 30
        else:
            if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
                mn = 1
                mx = 32
            else :
                mn = 1
                mx = 31
        for j in range (mn, mx) :
            a = []
            for i in range (1, 10) :
                a.append (randint(min_sal, max_sal))
                if index % 2 == 0:
                    large = second_largest(a)
                else:
                    large = max(a)
            f.write(job + ',' + str(str(index) + '-' + str(mon) + '-'+str(j)) + ',' + str (large) + ',' + str(min (a)) +'\n')

job = "Plumber"
min_sal = 250
max_sal = 500
for index in range (2000, 2017) :
    for mon in range (1, 13):
        if mon == 2 :
            if index % 4 != 0 :
                mn = 1
                mx = 29
            else :
                mn = 1
                mx = 30
        else:
            if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
                mn = 1
                mx = 32
            else :
                mn = 1
                mx = 31
        for j in range (mn, mx) :
            a = []
            for i in range (1, 10) :
                a.append (randint(min_sal, max_sal))
                if index % 2 == 0:
                    large = second_largest(a)
                else:
                    large = max(a)
            f.write(job + ',' + str(str(index) + '-' + str(mon) + '-'+str(j)) + ',' + str (large) + ',' + str(min (a)) +'\n')

job = "Mechanic"
min_sal = 400
max_sal = 650
for index in range (2000, 2017) :
    for mon in range (1, 13):
        if mon == 2 :
            if index % 4 != 0 :
                mn = 1
                mx = 29
            else :
                mn = 1
                mx = 30
        else:
            if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
                mn = 1
                mx = 32
            else :
                mn = 1
                mx = 31
        for j in range (mn, mx) :
            a = []
            for i in range (1, 10) :
                a.append (randint(min_sal, max_sal))
                if index % 2 == 0:
                    large = second_largest(a)
                else:
                    large = max(a)
            f.write(job + ',' + str(str(index) + '-' + str(mon) + '-'+str(j)) + ',' + str (large) + ',' + str(min (a)) +'\n')

f.close()
