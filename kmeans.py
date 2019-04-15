import random
base_list = [22,9,12,15,10,27,35,18,36,11]
t_list = [22,9,12,15,10,27,35,18,36,11]
k = int(input("Enter the no of clusters i.e value of k"))
clusters = list()
centroid = list()
#randomly select k points from the base_table
for i in range(k):
    centroid.append(random.choice(t_list))
    t_list.remove(centroid[i])
print(centroid)
while True:
    for i in range(k):
        clusters.append(list())
    for x in base_list:
        dummy = list()
        for y in centroid:
            dummy.append(abs(x-y))
        mini = dummy.index(min(dummy))
        clusters[mini].append(x)
    
    mean = list()
    for i in clusters:
        mean.append(sum(i)/len(i))
    print(mean)
    if centroid == mean:
        break
    else:
        clusters.clear()
        centroid = list()
        for ele in mean:
            centroid.append(ele)
print("got same means of two iterations so stopped")
print('final clusters')
print(clusters)
