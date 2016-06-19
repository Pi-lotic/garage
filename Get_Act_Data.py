import datetime 
import time
import sys

d=open('DATA/temperAct.csv')
data=d.readlines()
d.close()
temp=data[0]

d=open('DATA/humiAct.csv')
data=d.readlines()
d.close()
humi=data[0]

d=open('DATA/timeAct.csv')
data=d.readlines()
d.close()
time=data[0]

datastr = time + ' ' + temp + '*C ' + humi + '% '

print datastr
