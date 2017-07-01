import pandas as pd
from random import randint
inp_data = pd.read_csv("test.csv");
f= open("other.csv","w+")

job_id = 1
job = "Tester"
min_price = 500
max_price = 950

for index,row in inp_data.iterrows():
    avg_price = (max_price - min_price) / 3
    tot_val_1 = int(min_price + avg_price)
    tot_val_2 = int(tot_val_1 + avg_price)

    randInt = randint(min_price, max_price)

    if randInt <= tot_val_1:
        sd = 10
    elif ((randInt > tot_val_1) and (randInt <= tot_val_2)):
        sd = 11
    else :
        sd = 01
    f.write (str(job_id) + ',' + str (job) + ',' + str(row["place"]) + ","  + str(row["lat"]) + "," + str(row["lng"]) +','+ str(sd) +','+ str(randInt) + "\n")



job_id = 2
job = "Engineer"
min_price = 600
max_price = 1100

for index,row in inp_data.iterrows():
    avg_price = (max_price - min_price) / 3
    tot_val_1 = int(min_price + avg_price)
    tot_val_2 = int(tot_val_1 + avg_price)

    randInt = randint(min_price, max_price)

    if randInt <= tot_val_1:
        sd = 10
    elif ((randInt > tot_val_1) and (randInt <= tot_val_2)):
        sd = 11
    else :
        sd = 01
    f.write (str(job_id) + ',' + str (job) + ',' + str(row["place"]) + ","  + str(row["lat"]) + "," + str(row["lng"]) +','+ str(sd) +','+ str(randInt) + "\n")


job_id = 3
job = "Designer"
min_price = 400
max_price = 900

for index,row in inp_data.iterrows():
    avg_price = (max_price - min_price) / 3
    tot_val_1 = int(min_price + avg_price)
    tot_val_2 = int(tot_val_1 + avg_price)

    randInt = randint(min_price, max_price)

    if randInt <= tot_val_1:
        sd = 10
    elif ((randInt > tot_val_1) and (randInt <= tot_val_2)):
        sd = 11
    else :
        sd = 01
    f.write (str(job_id) + ',' + str (job) + ',' + str(row["place"]) + ","  + str(row["lat"]) + "," + str(row["lng"]) +','+ str(sd) +','+ str(randInt) + "\n")


job_id = 4
job = "Plumber"
min_price = 250
max_price = 500

for index,row in inp_data.iterrows():
    avg_price = (max_price - min_price) / 3
    tot_val_1 = int(min_price + avg_price)
    tot_val_2 = int(tot_val_1 + avg_price)

    randInt = randint(min_price, max_price)

    if randInt <= tot_val_1:
        sd = 10
    elif ((randInt > tot_val_1) and (randInt <= tot_val_2)):
        sd = 11
    else :
        sd = 01
    f.write (str(job_id) + ',' + str (job) + ',' + str(row["place"]) + ","  + str(row["lat"]) + "," + str(row["lng"]) +','+ str(sd) +','+ str(randInt) + "\n")


job_id = 5
job = "Carpenter"
min_price = 300
max_price = 450

for index,row in inp_data.iterrows():
    avg_price = (max_price - min_price) / 3
    tot_val_1 = int(min_price + avg_price)
    tot_val_2 = int(tot_val_1 + avg_price)

    randInt = randint(min_price, max_price)

    if randInt <= tot_val_1:
        sd = 10
    elif ((randInt > tot_val_1) and (randInt <= tot_val_2)):
        sd = 11
    else :
        sd = 01
    f.write (str(job_id) + ',' + str (job) + ',' + str(row["place"]) + ","  + str(row["lat"]) + "," + str(row["lng"]) +','+ str(sd) +','+ str(randInt) + "\n")


job_id = 6
job = "Painter"
min_price = 350
max_price = 700

for index,row in inp_data.iterrows():
    avg_price = (max_price - min_price) / 3
    tot_val_1 = int(min_price + avg_price)
    tot_val_2 = int(tot_val_1 + avg_price)

    randInt = randint(min_price, max_price)

    if randInt <= tot_val_1:
        sd = 10
    elif ((randInt > tot_val_1) and (randInt <= tot_val_2)):
        sd = 11
    else :
        sd = 01
    f.write (str(job_id) + ',' + str (job) + ',' + str(row["place"]) + ","  + str(row["lat"]) + "," + str(row["lng"]) +','+ str(sd) +','+ str(randInt) + "\n")


job_id = 7
job = "Waiter"
min_price = 200
max_price = 475

for index,row in inp_data.iterrows():
    avg_price = (max_price - min_price) / 3
    tot_val_1 = int(min_price + avg_price)
    tot_val_2 = int(tot_val_1 + avg_price)

    randInt = randint(min_price, max_price)

    if randInt <= tot_val_1:
        sd = 10
    elif ((randInt > tot_val_1) and (randInt <= tot_val_2)):
        sd = 11
    else :
        sd = 01
    f.write (str(job_id) + ',' + str (job) + ',' + str(row["place"]) + ","  + str(row["lat"]) + "," + str(row["lng"]) +','+ str(sd) +','+ str(randInt) + "\n")

job_id = 8
job = "Barber"
min_price = 150
max_price = 350

for index,row in inp_data.iterrows():
    avg_price = (max_price - min_price) / 3
    tot_val_1 = int(min_price + avg_price)
    tot_val_2 = int(tot_val_1 + avg_price)

    randInt = randint(min_price, max_price)

    if randInt <= tot_val_1:
        sd = 10
    elif ((randInt > tot_val_1) and (randInt <= tot_val_2)):
        sd = 11
    else :
        sd = 01
    f.write (str(job_id) + ',' + str (job) + ',' + str(row["place"]) + ","  + str(row["lat"]) + "," + str(row["lng"]) +','+ str(sd) +','+ str(randInt) + "\n")

job_id = 9
job = "Cleaner"
min_price = 250
max_price = 350

for index,row in inp_data.iterrows():
    avg_price = (max_price - min_price) / 3
    tot_val_1 = int(min_price + avg_price)
    tot_val_2 = int(tot_val_1 + avg_price)

    randInt = randint(min_price, max_price)

    if randInt <= tot_val_1:
        sd = 10
    elif ((randInt > tot_val_1) and (randInt <= tot_val_2)):
        sd = 11
    else :
        sd = 01
    f.write (str(job_id) + ',' + str (job) + ',' + str(row["place"]) + ","  + str(row["lat"]) + "," + str(row["lng"]) +','+ str(sd) +','+ str(randInt) + "\n")

job_id = 10
job = "Driver"
min_price = 450
max_price = 650

for index,row in inp_data.iterrows():
    avg_price = (max_price - min_price) / 3
    tot_val_1 = int(min_price + avg_price)
    tot_val_2 = int(tot_val_1 + avg_price)

    randInt = randint(min_price, max_price)

    if randInt <= tot_val_1:
        sd = 10
    elif ((randInt > tot_val_1) and (randInt <= tot_val_2)):
        sd = 11
    else :
        sd = 01
    f.write (str(job_id) + ',' + str (job) + ',' + str(row["place"]) + ","  + str(row["lat"]) + "," + str(row["lng"]) +','+ str(sd) +','+ str(randInt) + "\n")

job_id = 11
job = "Beautician"
min_price = 170
max_price = 350

for index,row in inp_data.iterrows():
    avg_price = (max_price - min_price) / 3
    tot_val_1 = int(min_price + avg_price)
    tot_val_2 = int(tot_val_1 + avg_price)

    randInt = randint(min_price, max_price)

    if randInt <= tot_val_1:
        sd = 10
    elif ((randInt > tot_val_1) and (randInt <= tot_val_2)):
        sd = 11
    else :
        sd = 01
    f.write (str(job_id) + ',' + str (job) + ',' + str(row["place"]) + ","  + str(row["lat"]) + "," + str(row["lng"]) +','+ str(sd) +','+ str(randInt) + "\n")

job_id = 12
job = "Mechanic"
min_price = 200
max_price = 420

for index,row in inp_data.iterrows():
    avg_price = (max_price - min_price) / 3
    tot_val_1 = int(min_price + avg_price)
    tot_val_2 = int(tot_val_1 + avg_price)

    randInt = randint(min_price, max_price)

    if randInt <= tot_val_1:
        sd = 10
    elif ((randInt > tot_val_1) and (randInt <= tot_val_2)):
        sd = 11
    else :
        sd = 01
    f.write (str(job_id) + ',' + str (job) + ',' + str(row["place"]) + ","  + str(row["lat"]) + "," + str(row["lng"]) +','+ str(sd) +','+ str(randInt) + "\n")

job_id = 13
job = "Photographer"
min_price = 270
max_price = 540

for index,row in inp_data.iterrows():
    avg_price = (max_price - min_price) / 3
    tot_val_1 = int(min_price + avg_price)
    tot_val_2 = int(tot_val_1 + avg_price)

    randInt = randint(min_price, max_price)

    if randInt <= tot_val_1:
        sd = 10
    elif ((randInt > tot_val_1) and (randInt <= tot_val_2)):
        sd = 11
    else :
        sd = 01
    f.write (str(job_id) + ',' + str (job) + ',' + str(row["place"]) + ","  + str(row["lat"]) + "," + str(row["lng"]) +','+ str(sd) +','+ str(randInt) + "\n")

f.close ()
