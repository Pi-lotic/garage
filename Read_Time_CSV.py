import sys
#TimeData=['2016-04-04 14:33:00,2016-04-04 14:34:00,2016-04-04 14:35:00,2016-04-04 14:36:00,']
Time=[]
d=open('time.csv')
data=d.readlines()
d.close()
datastr=data[0]
print datastr.count(',')
for i in range(datastr.count(',')+1):
    data1=datastr.partition(',')
    if data1[0]!= "":        
        Time.append(data1[0])
    datastr=data1[2]
#print datastr
print Time
