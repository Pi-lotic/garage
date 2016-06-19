import sys


Data_str=str(1.2)+","
try:
    d=open('data.csv','a+')
except:
    print 'kein Zugriff'
    sys.exit(0)
d.write(Data_str)
d.close()
