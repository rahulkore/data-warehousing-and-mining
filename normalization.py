import pandas as pd
df = pd.read_csv('car.csv')
x=df['wheel-base']
y=df['price']
x_bar = sum(x)/len(x)
y_bar = sum(y)/len(y)
numerator = 0
d1,d2=0,0
for xi,yi in zip(x,y):
    numerator = numerator + (xi-x_bar)*(yi-y_bar)
    d1 = d1 + (xi-x_bar)**2
    d2 = d2 + (yi-y_bar)**2
d1 = d1**(0.5)
d2 = d2**(0.5)
denominator = d1*d2
result = numerator/denominator
print("Pearson Coefficient:"+"\n")
print(result)#pearson coefficient


data = df['peak-rpm']
normalized_data = list()
#max-min
newmax,newmin = 100,0
for d in data:
    normalized_data.append(((d-min(data))/(max(data)-min(data)))*(newmax-newmin)+newmin)
print("max-min Normalized data"+"\n")
print(normalized_data)

#z-score
n_d=list()
n=0
mean = sum(data)/len(data)
for d in data:
    n = n + (d-mean)
n = n**0.5
sd = n/(len(data)-1)
for d in data:
    n_d.append((d-mean)/sd)
print("Z-score normalized data"+"\n")
print(n_d)

#decimal
n_d1=list()
dummy = ""
length = 0
for d in data:
    dummy = str(d)
    length = len(dummy)
    n_d1.append(d/((10)**length))
print("decimal Normalized data "+"\n")
print(n_d1)
