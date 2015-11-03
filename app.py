from flask import Flask
import saxsAnalyzer
import json
from nvd3 import lineWithFocusChart
from nvd3 import lineChart
from io import StringIO
app = Flask(__name__)


@app.route("/")
def index():
    chart = lineWithFocusChart(
        height=600, width='800', show_legend=False, name='lineWithFocusChart')
    data = saxsAnalyzer.getdata(5)
    for index, saxsdata in enumerate(data):
        chart.add_serie(name="Serie " + str(index),
                        y=saxsdata[1], x=range(len(saxsdata[1])))
    chart.buildhtml()
    return chart.htmlcontent


@app.route("/saxs")
def circlegathering():
    data = saxsAnalyzer.getdata(5)
    json = "["
    for index,saxsdata in enumerate(data):
        I = saxsdata[1]
        Q = saxsdata[0]
        for ivalue,qvalue in zip(I,Q):
            json += "{\"name\": \"Azimuthal " + str(index) + "\"" + ", \"Q\" :" +str(qvalue) + ", \"I\" :" + str(ivalue) + "},"
        json += "]"
    return json

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
