import sys

temp=[1,1.7,2.1]
Data_str=str(temp[0])
for i in range(len(temp)-1):
    Data_str+=","+str(temp[i+1])
try:
    d=open('data.csv','w')
except:
    print 'kein Zugriff'
    sys.exit(0)
d.write(Data_str)
d.close()
