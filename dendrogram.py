import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("dat.csv")
data = list()
for x,y in zip(df["attribute1"],df["attribute2"]):
    temp = list()
    temp.append(x)
    temp.append(y)
    data.append(temp)

from scipy.cluster.hierarchy import dendrogram, linkage
Z = linkage(data,method="ward")
dendrogram(Z)
from sklearn.cluster import AgglomerativeClustering
k = int(input("Enter the no of clusters to form:"))
cluster=AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='ward')  
cluster.fit_predict(data)
print(cluster.labels_)