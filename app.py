from flask import Flask

app = Flask(__name__)

def Fkt_Test:
    test='Fkt_Test'
    return test

@app.route('/')
def index():
    # test='Hi Babsimausi'
    
    return Fkt_Test



@app.route('/test')
def test():
    test='TEST'
    return str(test)
if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')
    


