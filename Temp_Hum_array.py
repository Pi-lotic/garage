import datetime 
import Adafruit_DHT
import time
ts = time.time()
while 1:

        time.sleep(2)
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
        if humidity is not None and temperature is not None:
                ta = time.time()
                st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                #print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
                print [ta-ts, temperature, humidity]
        else:
                print ('Failed to get reading. Try again!')
