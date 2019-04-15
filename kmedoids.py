def error_rate():
    error = 0
    for x in d_list:
        error = error + min(x)
    return error
import random
base_list = [[2,6],[3,4],[3,8],[4,7],[6,2],[6,4],[7,3],[7,4],[8,5],[7,6]]
t_list = [[2,6],[3,4],[3,8],[4,7],[6,2],[6,4],[7,3],[7,4],[8,5],[7,6]]
k = int(input("Enter the no of clusters i.e value of k"))
clusters = list()
clusters_numbering = list()
centroid = list()
index_list = list()
prev_cent = list()
#randomly select k points from the base_table

for i in range(k):
    centroid.append(random.choice(t_list))
    index_list.append(base_list.index(centroid[i]))
    t_list.remove(centroid[i])
'''
centroid.append(base_list[1])
centroid.append(base_list[7])
index_list.append(1)
index_list.append(7)
'''
print(centroid)
#print(prev_cent)
d_list = list()
prev_error = 32767
def kmedoids(centroid):
    for i in range(k):
        clusters.append(list())
    for x in base_list:
        dummy = list()
        for y in centroid:
            dummy.append(abs(x[0]-y[0]) + abs(x[1]-y[1]))
        mini = dummy.index(min(dummy))
        d_list.append(dummy)
        clusters_numbering.append(mini)
    #print(clusters_numbering)
    for i,element in zip(clusters_numbering,base_list):
        clusters[i].append(element)
    print(clusters)
    error = error_rate()
    
    return error
while True:
    error = kmedoids(centroid)
    print(error)
    if prev_error < error:
        clusters_numbering.clear()
        clusters.clear()
        d_list.clear()
        print("final centroids:")
        print(prev_cent)
        print("final clusters:")
        error = kmedoids(prev_cent)
        break
    prev_error = error
    #print(error)
    prev_cent.clear()
    for ele in centroid:
        prev_cent.append(ele)
    temp = centroid[len(centroid)-1]
    centroid.remove(centroid[len(centroid)-1])
    centroid.append(base_list[base_list.index(temp)-1])
    print(centroid)
    #centroid.append(base_list[6])
    clusters_numbering.clear()
    clusters.clear()
    d_list.clear()