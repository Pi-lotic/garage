from flask import Flask
from flask import render_template
from flask import request

import RPi.GPIO as GPIO

import datetime 
import Adafruit_DHT
import time

class Klima:
    TempData=[1] #Eigenschaften
    HumyData=[1] #Eigenschaften
    Temp=[1]
    i=0
    def add_Temp(self,wert):
        self.Temp[0] = wert
        self.TempData += self.Temp
    def add_Humy(self,wert):
        self.Temp[0] = wert
        self.HumyData += self.Temp
    def ausgabe(self):
        print(self.TempData, self.HumyData)
    def get_Temp(self):
        return self.TempData
    def get_Humy(self):
        return self.HumyData
    
Buro=Klima()
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
#while 1:
#    time.sleep(10)
#    Buro.ausgabe()


app = Flask(__name__)

@app.route('/hello', methods=['POST','GET'])
#@app.route('/hello')

def hello(TempHum=None):
    if request.method == 'GET':
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
        
        if humidity is not None and temperature is not None:
            Buro.add_Temp = temperature
            Buro.add_Humy = humidity
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

@app.route('/Chart')

def Chart(chartID = 'chart_ID', chart_type = 'line', chart_height = 500,TempData=[22,23,24]):
    
    HumyData=[42.2,43,44.5]
    Buro.ausgabe()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Temperatur', "data": TempData}, {"name": 'Luftfeuchte', "data": HumyData}]
    title = {"text": 'Klima'}
    xAxis = {"categories": ['0']}
    yAxis = {"title": {"text": 'Temp[*C] Humidity[%]'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)



if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, passthrough_errors=True)
    



