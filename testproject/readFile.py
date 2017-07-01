import re
with open ("file.txt", "r") as myfile:
    data=myfile.read().replace('moreaddress(', '')
    data = data.replace ('"Bangalore");', '')
    data = data.replace ('"', '')
    data = data.replace (' ', '')
    data = data.replace(',\n\n','\n')
    data = re.sub(r',Pin-\d*', "", data)
    print data

'''Write out put to file
#python readFile.py > test.csv
'''
