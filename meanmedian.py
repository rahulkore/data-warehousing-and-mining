import pandas as pd
df = pd.read_csv("dwm1.csv")
result = df["ce"]

def writefile(text):
  file_handle = open("result.txt","a")
  file_handle.write(text+"\n")

#finding mean
mean = sum(result)/len(result)
writefile("Mean ="+str(mean))

#median
if len(result)%2==0:
  median = (result[len(result)/2]+result[(len(result)/2)-1])/2
else:
  median = result[len(result)/2]
writefile("Median ="+str(median))

#finding range
data_range = max(result)-min(result)
writefile("Range ="+str(data_range))

#finding mode
maxcount,maxvalue = 0,0
for i in range(len(result)):
  count = 0
  for j in range(len(result)):
    if result[j] == result[i]:
      count+=1
  if count > maxcount:
    maxcount = count
    maxvalue = result[i]
mode = maxvalue
writefile("Mode ="+str(mode))