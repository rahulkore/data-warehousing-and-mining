import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
a,b,c,d=0,0,0,0
df =  pd.read_csv("matches.csv")
for match in df["season"]:
    if match == 2008:
        a+=1
    elif match == 2009:
        b+=1
    elif match == 2010:
        c+=1
    elif match == 2011:
        d+=1
x=df["id"]
y=df["win_by_wickets"]
#print(x)
#print(y)
x = list(map(int, x))
y= list(map(int, y))

#scatter plot
plt.scatter(x,y,label="ball vs runs")
plt.show()
labels = '2008', '2009','2010', '2011'
sizes = [a, b, c, d]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)

#pie plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.show()

#bar plot
plt.bar(labels, sizes, align='center', alpha=0.5)
plt.xlabel('Season Year')
plt.ylabel('Number of matches')
plt.show()

#line plot
plt.plot(sizes)
plt.show()

#hist plot
plt.hist(sizes, 50, density=1, facecolor='g', alpha=0.75)
plt.show()


#plot hist of our own data
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

#box plot
plt.boxplot(x)
plt.show()
