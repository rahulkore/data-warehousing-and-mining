import pandas as pd
import operator
def sort(boolean,data_dict):
    data_dict = sorted(data_dict.items(), key=operator.itemgetter(1),reverse=boolean)
    data_list = list()
    dict_ = dict()
    for x in data_dict:
        dict_[x[0]] = x[1]
    return dict_

def del_less_than_min_sup():
    remove = list()
    for ele in data_dict:
        if data_dict[ele]<min_sup:
            remove.append(ele)
    for ele in remove:
        del data_dict[ele]
df = pd.read_csv("apriori2.csv")
item_list = df["items"]
data = list()
for ele in item_list:
    data.append(ele.split(","))
min_sup = int(input("Enter minimum support:"))
data_dict = dict()
print("Given data")
print(data)
data_dict = dict()
for x in data:
    for ele in x:
        if ele not in data_dict:
            data_dict[ele] = 1
        else:
            data_dict[ele] += 1
del_less_than_min_sup()
data_dict = sort(True,data_dict)

print(data_dict)
intermediate_data = list()
for x in data:
    temp = list()
    for ele in data_dict:
        if ele in x:
            temp.append(ele)
    intermediate_data.append(temp)
print("new data")
print(intermediate_data)

#nodes of fptree
class node:
    def __init__(self,name,count,parent):
        self.name = name
        self.count = count
        self.parent = parent
        self.children = {}
    def inc_counter(self):
        self.count += 1

#generating the tree
node_objects = list()
for ele,index in zip(intermediate_data[0],range(len(intermediate_data[0]))):
    if index == 0:
        node_objects.append(node(ele,1,None))
    else:
        node_objects.append(node(ele,1,intermediate_data[0][index-1]))
intermediate_data.pop(0)
for x in intermediate_data:
    i = 0
    flag = 0
    for ele,index in zip(x,range(len(x))):
        if ele == node_objects[i].name and flag == i:
            node_objects[i].inc_counter()
            flag += 1
        else:
            node_objects.append(node(ele,1,x[index-1]))
        i += 1
print("-----------------FP tree---------------")
for i in range(len(node_objects)):
    print(node_objects[i].name,node_objects[i].count,node_objects[i].parent)
#generating conditional pattern base
data_dict = sort(False,data_dict)
#print(data_dict)
conditional_pattern_base = dict()
def find_parents(i,parent,count,x):
    if node_objects[i].parent == None:
        if node_objects[i].name not in parent:
            parent = parent + "," + node_objects[i].name
        temp = [parent,count]
        conditional_pattern_base[x].append(temp)
        return 
    if node_objects[i].parent == node_objects[i-1].name:
        parent = parent + "," + node_objects[i].parent
        find_parents(i-1,parent,count,x)
    else:
        for ele in node_objects:
            if node_objects[i].parent == ele.name:
                parent = parent + "," + node_objects[i].parent
                break
        find_parents(node_objects.index(ele),parent,count,x)
            
for x in list(data_dict.keys()):
    i = 0
    conditional_pattern_base[x] = list()
    while i<len(node_objects):
        if x == node_objects[i].name:
            #print(node_objects[i].name)
            if node_objects[i].parent == None:
                break
            find_parents(i,"",node_objects[i].count,x)
        i += 1
print("---------conditional pattern base is as shown below---------")
print(conditional_pattern_base)

#constructing conditional fp
conditional_fp = dict()
def condi_fp(index,element,flag):
    for y in conditional_pattern_base[index]:
        t = y[0].split(",")
        t.pop(0)
        z=list(set(element).intersection(set(t)))
        if flag == 0:
            for i in z:
                if i not in conditional_fp[index]:
                    conditional_fp[index][i] = 0 + y[1]
                else:
                    conditional_fp[index][i] = conditional_fp[index][i] + y[1]
        length = 0 
        while length < len(element):
            tt = list()
            string = ""
            for i in range(length+1):
                tt.append(element[i])
                string = string + element[i]
            if all(c in t for c in tt) and len(tt) != 1:
                if string not in conditional_fp[index]:
                    conditional_fp[index][string] = 0 + y[1]
                else:
                    conditional_fp[index][string] = conditional_fp[index][string] + y[1]
            length += 1
    flag = 1
    return flag
for x in conditional_pattern_base:
    conditional_fp[x] = dict()
    flag = 0
    for ele in conditional_pattern_base[x]:
        temp = ele[0].split(",")
        temp.pop(0)
        flag = condi_fp(x,temp,flag)
#removing all the values having support less than min_support from conditional_fp

for x in conditional_fp:
    inner_keys = list(conditional_fp[x].keys())
    for key in inner_keys:
        if conditional_fp[x][key] < min_sup:
            del conditional_fp[x][key]
print("----------conditional fp is asshown below----------")
print(conditional_fp)