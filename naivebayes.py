import pandas as pd
from collections import defaultdict
df =pd.read_csv("data.csv")
def info_gain(llist):
    result = dict()
    for data in llist:
        if data not in result:
            result[data] = 1
        else:
            result[data] +=1
    return result

attr = list(df.keys())
total = df[attr[len(attr)-1]].count()
k = info_gain(df[attr[len(attr)-1]])
values = k.values()
class_values = k.keys()
p = dict()
for key in class_values:
    p[key] = k[key]/total
print("probability of output class tupples"+"\n")
print(p)
l = list()
for d in df["height"]:
    if d <= 1.7:
        l.append("a")
    if d >= 2:
        l.append("b")
    if d > 1.7 and d < 2:
        l.append("c")
df["height"] = l
df.drop(['name'],axis=1)
#print(df)
#test = list(input().split())
# we are building the model for <rohit,male(m),1.95>
gender = defaultdict(dict)
height = defaultdict(dict)
for d1,d2,d3 in zip(df['gender'],df['height'],df['output']):
    if d1 == 'm':
        gender[d1][d3] = 0
    if d2 == 'c':
        height[d2][d3] = 0

for d1,d2,d3 in zip(df['gender'],df['height'],df['output']):
    if d1 == 'm':
        gender[d1][d3] += 1
    if d2 == 'c':
        height[d2][d3] += 1
#print(gender)
#print(height)
g_keys = gender.keys()
h_keys = height.keys()
for_result = list()
result = dict()
for d1,d2 in zip(g_keys,h_keys):
    for inner_key in class_values:
        if inner_key in gender[d1]:
            x1 = gender[d1][inner_key]/k[inner_key]
        else:
            x1 = 0
        if inner_key in height[d2]:
            x2 = height[d2][inner_key]/k[inner_key]
        else:
            x2 = 0
        for_result.append(x1*x2)
print("\nIntermediate result\n")
print(for_result)
for key,fr in zip(class_values,for_result):
    result[key] = p[key]*fr
print("\nfinal output\n")
print(result)