import pandas as pd
import math
from collections import defaultdict
df = pd.read_csv("Book1.csv")
def info_gain(llist):
    result = dict()
    for data in llist:
        if data not in result:
            result[data] = 1
        else:
            result[data] +=1
    return result
#global for_result=0
def info_gain_attr(slist,llist,total):
    result = defaultdict(dict)
    
    for data1,data2 in zip(slist,llist):
        result[data1][data2] = 0
    #print(result)
    for data1,data2 in zip(slist,llist):
        result[data1][data2] += 1
    key = result.keys()
    inner_key = set(llist)
    inner_key = list(inner_key)
    print(result)
    print(inner_key)
    main_result = 0
    for data in key:
        st=0
        for inner_data in inner_key:
            if inner_data in result[data]:
                st = st + result[data][inner_data]
        inf_a = 0
        print(st)
        for inner_data in inner_key:
            if inner_data in result[data]:
                
                inf_a = inf_a - (st/total)*(result[data][inner_data]/st)*math.log(result[data][inner_data]/st,2)
        main_result = main_result + inf_a
    
    
    return main_result
attr = list(df.keys())
k = info_gain(df[attr[len(attr)-1]])
f = k.values()
total = sum(f)
inf_d = 0
for data in f:
    inf_d = inf_d - (data/total)*math.log((data/total),2)
d1_result=list()
for d in range(len(attr)-1):
    d_result = info_gain_attr(df[attr[d]],df[attr[len(attr)-1]],total)
    d1_result.append(d_result)
for d in range(len(d1_result)):
    d1_result[d] = inf_d - d1_result[d] 
d1_result = sorted(d1_result,reverse=True)
print(d1_result)