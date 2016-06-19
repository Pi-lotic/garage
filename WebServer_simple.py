from flask import Flask
from flask import render_template
from flask import request

import RPi.GPIO as GPIO

import datetime 
import Adafruit_DHT
import time

#OptoIn    = 21
Switch_K1 = 13
Switch_K2 = 15
#Switch_K4 = 11

# Initialize IO
GPIO.setmode(GPIO.BOARD)
#GPIO.setup (OptoIn, GPIO.IN)
#GPIO.setup (Switch_K4, GPIO.OUT)
GPIO.setup (Switch_K2, GPIO.OUT)
GPIO.setup (Switch_K1, GPIO.OUT)

# Set all Ouputs OFF
GPIO.output(Switch_K1, GPIO.HIGH)
GPIO.output(Switch_K2, GPIO.HIGH)
#GPIO.output(Switch_K4, GPIO.HIGH)



app = Flask(__name__)

@app.route('/hello', methods=['POST','GET'])
#@app.route('/hello')

def hello(TempHum=None):
    if request.method == 'GET':
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)        
        if humidity is not None and temperature is not None:
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            text= st + ' {0:0.1f}*C {1:0.1f}%'.format(temperature, humidity)
        else:
            text= 'Failed to get reading. Try again!'
        return render_template('simple.html',TempHum=text)
        return render_template('simple.html',TempHum=TempHum)
    
        if request.method == 'POST':
            text='post_message'
        return render_template('simple.html',TempHum=text)
    return render_template('simple.html',TempHum=TempHum)

#app = Flask(__name__)

@app.route('/LampeAus',methods=['POST','GET'])

def LampeAus():
    if request.method == 'GET':
        GPIO.output(Switch_K1, GPIO.LOW)    # Lampe AUS
        GPIO.output(Switch_K2, GPIO.HIGH)    # Lampe AUS
        return render_template('test.html')
    return render_template('test.html')

@app.route('/LampeEin',methods=['POST','GET'])

def LampeEin():
    GPIO.output(Switch_K1, GPIO.HIGH)    # Lampe EIN
    GPIO.output(Switch_K2, GPIO.LOW)    # Lampe AUS
    return render_template('test.html')

if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')
    



