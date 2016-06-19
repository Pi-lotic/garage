from flask import Flask
from flask import render_template
from flask import request

import Adafruit_DHT


app = Flask(__name__)

@app.route('/hello', methods=['POST','GET'])
#@app.route('/hello')

def hello(TempHum=None):
    if request.method == 'GET':
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
        if humidity is not None and temperature is not None:
            text= 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
        else:
            text= 'Failed to get reading. Try again!'
        return render_template('hello.html',TempHum=text)
        return render_template('hello.html',TempHum=TempHum)
    
    if request.method == 'POST':
        
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
        if humidity is not None and temperature is not None:
            text= 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
        else:
            text= 'Failed to get reading. Try again!'
        return render_template('hello.html',TempHum=text)
    return render_template('hello.html',TempHum=TempHum)

#app = Flask(__name__)

@app.route('/test')

def test():
    return render_template('test.html')

if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')
    



