import pandas as pd
import numpy as np
from random import randint

dateList = ['2000-01', '2000-02', '2000-03', '2000-04', '2000-05', '2000-06', '2000-07', '2000-08', '2000-09', '2000-10', '2000-11', '2000-12',
            '2001-01', '2001-02', '2001-03', '2001-04', '2001-05', '2001-06', '2001-07', '2001-08', '2001-09', '2001-10', '2001-11', '2001-12',
            '2002-01', '2002-02', '2002-03', '2002-04', '2002-05', '2002-06', '2002-07', '2002-08', '2002-09', '2002-10', '2002-11', '2002-12',
            '2003-01', '2003-02', '2003-03', '2003-04', '2003-05', '2003-06', '2003-07', '2003-08', '2003-09', '2003-10', '2003-11', '2003-12',
            '2004-01', '2004-02', '2004-03', '2004-04', '2004-05', '2004-06', '2004-07', '2004-08', '2004-09', '2004-10', '2004-11', '2004-12',
            '2005-01', '2005-02', '2005-03', '2005-04', '2005-05', '2005-06', '2005-07', '2005-08', '2005-09', '2005-10', '2005-11', '2005-12',
            '2006-01', '2006-02', '2006-03', '2006-04', '2006-05', '2006-06', '2006-07', '2006-08', '2006-09', '2006-10', '2006-11', '2006-12',
            '2007-01', '2007-02', '2007-03', '2007-04', '2007-05', '2007-06', '2007-07', '2007-08', '2007-09', '2007-10', '2007-11', '2007-12',
            '2008-01', '2008-02', '2008-03', '2008-04', '2008-05', '2008-06', '2008-07', '2008-08', '2008-09', '2008-10', '2008-11', '2008-12',
            '2009-01', '2009-02', '2009-03', '2009-04', '2009-05', '2009-06', '2009-07', '2009-08', '2009-09', '2009-10', '2009-11', '2009-12',
            '2010-01', '2010-02', '2010-03', '2010-04', '2010-05', '2010-06', '2010-07', '2010-08', '2010-09', '2010-10', '2010-11', '2010-12',
	        '2011-01', '2011-02', '2011-03', '2011-04', '2011-05', '2011-06', '2011-07', '2011-08', '2011-09', '2011-10', '2011-11', '2011-12',
	        '2012-01', '2012-02', '2012-03', '2012-04', '2012-05', '2012-06', '2012-07', '2012-08', '2012-09', '2012-10', '2012-11', '2012-12',
            '2013-01', '2013-02', '2013-03', '2013-04', '2013-05', '2013-06', '2013-07', '2013-08', '2013-09', '2013-10', '2013-11', '2013-12'
            ]
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
for index in range (0,168) :
    a = []
    for i in range (1, 10) :
        a.append (randint(min_sal, max_sal))
    if index % 2 == 0:
        large = second_largest(a)
    else:
        large = max(a)
    f.write(str(dateList[index]+'-01') + ',' + str (large)  +'\n')

'''
job = "Tester"
min_sal = 400
max_sal = 900
for index in range (0,156) :
    a = []
    for i in range (1, 10) :
        a.append (randint(min_sal, max_sal))
    if index % 2 == 0:
        large = second_largest(a)
    else:
        large = max(a)
    f.write(job + ',' + str(dateList[index]+'01') + ',' + str (large) + ',' + str(min (a)) +'\n')


job = "Photographer"
min_sal = 450
max_sal = 700
for index in range (0,156) :
    a = []
    for i in range (1, 10) :
        a.append (randint(min_sal, max_sal))
    if index % 2 == 0:
        large = second_largest(a)
    else:
        large = max(a)
    f.write(job + ',' + str(dateList[index]+'01') + ',' + str (large) + ',' + str(min (a)) +'\n')


job = "Carpenter"
min_sal = 350
max_sal = 700
for index in range (0,156) :
    a = []
    for i in range (1, 10) :
        a.append (randint(min_sal, max_sal))
    if index % 2 == 0:
        large = second_largest(a)
    else:
        large = max(a)
    f.write(job + ',' + str(dateList[index]+'01') + ',' + str (large) + ',' + str(min (a)) +'\n')


job = "Cook"
min_sal = 400
max_sal = 800
for index in range (0,156) :
    a = []
    for i in range (1, 10) :
        a.append (randint(min_sal, max_sal))
    if index % 2 == 0:
        large = second_largest(a)
    else:
        large = max(a)
    f.write(job + ',' + str(dateList[index]+'01') + ',' + str (large) + ',' + str(min (a)) +'\n')


job = "Plumber"
min_sal = 250
max_sal = 500
for index in range (0,156) :
    a = []
    for i in range (1, 10) :
        a.append (randint(min_sal, max_sal))
    if index % 2 == 0:
        large = second_largest(a)
    else:
        large = max(a)
    f.write(job + ',' + str(dateList[index]+'01') + ',' + str (large) + ',' + str(min (a)) +'\n')


job = "Mechanic"
min_sal = 400
max_sal = 650
for index in range (0,156) :
    a = []
    for i in range (1, 10) :
        a.append (randint(min_sal, max_sal))
    if index % 2 == 0:
        large = second_largest(a)
    else:
        large = max(a)
    f.write(job + ',' + str(dateList[index]+'01') + ',' + str (large) + ',' + str(min (a)) +'\n')
'''
f.close()
