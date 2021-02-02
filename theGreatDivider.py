# Welcome to theGreatDivider.py!

# This app reads a CSV-file-path and devide the content according to your specifications
# Plans are to expand this to return a new CSV or a .txt-file, if there is time..

import csv
import random


file_path = input("\nWrite the path to the file here: \n")

newList = []

with open(file_path) as f:
    d = csv.reader(f)
    for i in d:
        newList.append(i)


formated_list = []
for member in newList:
    for row in member:
        row = row.replace(";","")
        row = row.replace(",","")
        if row == "" or row == " ":
            n = newList.index(member)
            newList.pop(n)
        else:
            formated_list.append(row)



random.shuffle(formated_list)

member_num = int(input("\nHow many people in every group? "))
final_list = [formated_list[x:x+member_num] for x in range(0,len(formated_list),member_num)]


for groups in final_list:
    print("\nGroup: {}".format(final_list.index(groups)+1))
    for member in groups:
        print(member.capitalize())