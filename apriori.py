import pandas as pd
def del_less_than_min_sup():
    remove = list()
    flag = 0
    for ele in data_dict:
        if data_dict[ele]<min_sup:
            flag = 1
            remove.append(ele)
    for ele in remove:
        del data_dict[ele]
    if flag == 1:
        return True
    else:
        return False
df = pd.read_csv("apriori.csv")
item_list = df["items"]
data = list()
for ele in item_list:
    data.append(ele.split(","))
min_sup = int(input("Enter minimum support:"))
data_dict = dict()
for x in data:
    for ele in x:
        if ele not in data_dict:
            data_dict[ele] = 1
        else:
            data_dict[ele] += 1
check = del_less_than_min_sup()
prev_data_list = list(data_dict.keys())
while True:
    data_list = list()
    data_dict = dict()
    for i in prev_data_list:
        for j in prev_data_list:
            if (i,j) and (j,i) not in data_list and i != j:
                temp = set(i.replace(","," ").split(" ") + j.replace(","," ").split(" "))
                temp = list(temp)
                if temp[0] == '':
                    temp.pop(0)
                if temp not in data_list:
                    data_list.append(temp)
    for ele in data_list:
        temp = list(ele)
        index = ""
        for x in temp:
            index = index  + "," + x
        for y in data:
            if all(x in y for x in temp):
                if index not in data_dict:
                    data_dict[index] = 1
                else:
                    data_dict[index] += 1
    check = del_less_than_min_sup()
    if check == False:
        print("Frequent patterns from the given data set is :")
        break
    prev_data_list = list()
    prev_data_list = list(data_dict.keys())
#for confidence of the frquent paterns
for_confidence = list()
for d in prev_data_list:
    temp = list()
    for dd in d.split(","):
        if dd != '':
            temp.append(dd)
    for_confidence.append(temp)
print(for_confidence)
for temp in for_confidence:
    numerator = 0
    for y in data:
        if all(x in y for x in temp):
            numerator += 1
    for ele in temp:
        deno = 0
        for y in data:
            if ele in y:
                deno+=1
        print("confidence for %s is"%ele)
        print(numerator/deno)import pandas as pd
def del_less_than_min_sup():
    remove = list()
    flag = 0
    for ele in data_dict:
        if data_dict[ele]<min_sup:
            flag = 1
            remove.append(ele)
    for ele in remove:
        del data_dict[ele]
    if flag == 1:
        return True
    else:
        return False
df = pd.read_csv("apriori.csv")
item_list = df["items"]
data = list()
for ele in item_list:
    data.append(ele.split(","))
min_sup = int(input("Enter minimum support:"))
data_dict = dict()
for x in data:
    for ele in x:
        if ele not in data_dict:
            data_dict[ele] = 1
        else:
            data_dict[ele] += 1
check = del_less_than_min_sup()
prev_data_list = list(data_dict.keys())
while True:
    data_list = list()
    data_dict = dict()
    for i in prev_data_list:
        for j in prev_data_list:
            if (i,j) and (j,i) not in data_list and i != j:
                temp = set(i.replace(","," ").split(" ") + j.replace(","," ").split(" "))
                temp = list(temp)
                if temp[0] == '':
                    temp.pop(0)
                if temp not in data_list:
                    data_list.append(temp)
    for ele in data_list:
        temp = list(ele)
        index = ""
        for x in temp:
            index = index  + "," + x
        for y in data:
            if all(x in y for x in temp):
                if index not in data_dict:
                    data_dict[index] = 1
                else:
                    data_dict[index] += 1
    check = del_less_than_min_sup()
    if check == False:
        print("Frequent patterns from the given data set is :")
        break
    prev_data_list = list()
    prev_data_list = list(data_dict.keys())
#for confidence of the frquent paterns
for_confidence = list()
for d in prev_data_list:
    temp = list()
    for dd in d.split(","):
        if dd != '':
            temp.append(dd)
    for_confidence.append(temp)
print(for_confidence)
for temp in for_confidence:
    numerator = 0
    for y in data:
        if all(x in y for x in temp):
            numerator += 1
    for ele in temp:
        deno = 0
        for y in data:
            if ele in y:
                deno+=1
        print("confidence for %s is"%ele)
        print(numerator/deno)