import datetime 
# import Adafruit_DHT
import time
import sys

# humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
humidity = 1.1
temperature = 2.3

if humidity is not None and temperature is not None:
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    text= st + ' {0:0.1f}*C {1:0.1f}%'.format(temperature, humidity)
    print text
#    d=open('DATA/temper.csv','a+')
#    d.write('{0:0.1f},'.format(temperature))
#    d.close()
    d=open('DATA/temperAct.csv','w')
    d.write('{0:0.1f}'.format(temperature))
    d.close()
    
#    d=open('DATA/humi.csv','a+')
#    d.write('{0:0.1f},'.format(humidity))
#    d.close()
    d=open('DATA/humiAct.csv','w')
    d.write('{0:0.1f}'.format(humidity))
    d.close()
    
#    d=open('DATA/time.csv','a+')
#    d.write(st+',')
#    d.close()
    d=open('DATA/timeAct.csv','w')
    d.write(st)
    d.close()             
else:
     text= 'Failed to get reading. Try again!'
