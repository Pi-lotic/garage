from flask import Flask
import Adafruit_DHT
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)

if humidity is not None and temperature is not None:
    text= 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
else:
    text= 'Failed to get reading. Try again!'
    
app = Flask(__name__)

@app.route('/')
def index():
    return str(text)
if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')
    
