from flask import Flask
from flask import render_template
from flask import request

import RPi.GPIO as GPIO

import datetime 
import Adafruit_DHT
import time, thread
import sys

#OptoIn    = 21
Switch_K1 = 13
Switch_K2 = 15
#Switch_K4 = 11

# Initialize IO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#GPIO.setup (OptoIn, GPIO.IN)
#GPIO.setup (Switch_K4, GPIO.OUT)
GPIO.setup (Switch_K2, GPIO.OUT)
GPIO.setup (Switch_K1, GPIO.OUT)

# Set all Ouputs OFF
GPIO.output(Switch_K1, GPIO.HIGH)
GPIO.output(Switch_K2, GPIO.HIGH)
#GPIO.output(Switch_K4, GPIO.HIGH)

# Funktion Schalten
def Taster_Funktion():
        GPIO.output(Switch_K1, GPIO.LOW)    # Lampe AUS
        GPIO.output(Switch_K2, GPIO.HIGH)   # Lampe AUS      
        time.sleep(1)
        GPIO.output(Switch_K1, GPIO.HIGH)   # Lampe EIN
        GPIO.output(Switch_K2, GPIO.LOW)    # Lampe AUS
        return

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])


def hello(TempHum=None):
        if request.method == 'GET':
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
#            d=open('time.csv','a+')
#            d.write(st+',')
#            d.close()             
        return render_template('simple.html',TempHum=st)
@app.route('/LampeAus',methods=['POST','GET'])

def LampeAus():
    if request.method == 'GET':
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')            
        thread.start_new_thread(Taster_Funktion,())
        return render_template('simple.html', TempHum=st)
    return render_template('simple.html', TempHum=st)

@app.route('/LampeEin',methods=['POST','GET'])

def LampeEin():
    return render_template('simple.html')

@app.route('/Chart')

def Chart(chartID = 'chart_ID', chart_type = 'line', chart_height = 500,TempData=[],HumyData=[],TimeScale=[]):
    #Temperaturen lesen
    d=open('temper.csv')
    data=d.readlines()
    d.close()
    datastr=data[0]
    for i in range(datastr.count(',')+1):
        data1=datastr.partition(',')
        if data1[0]!= "":
            TempData.append(float(data1[0]))
        datastr=data1[2]
        
    #Feuchtigkeitswerte lesen
    d=open('humi.csv')
    data=d.readlines()
    d.close()
    datastr=data[0]
    for i in range(datastr.count(',')+1):
        data1=datastr.partition(',')
        if data1[0]!= "":
            HumyData.append(float(data1[0]))
        datastr=data1[2]
        
    #Zeitstempel lesen
    d=open('time.csv')
    data=d.readlines()
    d.close()
    datastr=data[0]
    for i in range(datastr.count(',')+1):
        data1=datastr.partition(',')
        if data1[0]!= "":        
            TimeScale.append(data1[0])
        datastr=data1[2]
    
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Temperatur', "data": TempData}, {"name": 'Luftfeuchte', "data": HumyData}]
    title = {"text": 'Klima'}
    xAxis = {"categories": TimeScale}
    yAxis = {"title": {"text": 'Temp[*C] Humidity[%]'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)



if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0', port=80, passthrough_errors=True)
    



