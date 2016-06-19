import datetime 
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
n=0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.IN)

ts = time.time()
tsb = time.time()
dt=1
while 1:

        time.sleep(2)
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
        if humidity is not None and temperature is not None:
                ta = time.time()
                st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                #print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
                print [ta-ts, temperature, humidity, 3600/dt]
        else:
                print ('Failed to get reading. Try again!')
        if GPIO.input(21) == GPIO.HIGH:
                old=1
        else:
                if old == 1:
                    tn= time.time()
                    dt=tn-tsb
                    tsb=tn
                    n=n+1
                    old=0
