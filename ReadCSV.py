import sys
TempData=[]

d=open('data.csv')
data=d.readlines()
d.close()
datastr=data[0]
for i in range(datastr.count(',')+1):
    data1=datastr.partition(',')
    if data1[0]!= "":        
        TempData.append(float(data1[0]))
    datastr=data1[2]
print datastr, TempData
