  
from flask import Flask, render_template
 
app = Flask(__name__)

@app.route('/')
def homepage():

    title = "Epic Tutorials"
    paragraph = ["wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!","wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!"]

    try:
        return render_template("index_2.html", title = title, paragraph=paragraph)
    except Exception, e:
        return str(e)

@app.route('/about')
def aboutpage():

    title = "About this site"
    paragraph = ["blah blah blah memememememmeme blah blah memememe"]

    pageType = 'about'

    return render_template("index_2.html", title=title, paragraph=paragraph, pageType=pageType)


@app.route('/about/contact')
def contactPage():

    title = "About this site"
    paragraph = ["blah blah blah memememememmeme blah blah memememe"]

    pageType = 'about'

    return render_template("index_2.html", title=title, paragraph=paragraph, pageType=pageType)



@app.route('/graph')
def graph(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	series = [{"name": 'Temperatur', "data": [3.1,2.2,1.3,-2,12]}, {"name": 'Luftfeuchte', "data": [4, 5, 6]}]
	title = {"text": 'Klima'}
	xAxis = {"categories": ['0']}
	yAxis = {"title": {"text": '*C %'}}
	return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
 
if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)

