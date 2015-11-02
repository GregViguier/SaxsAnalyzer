from flask import Flask
from flask import render_template
import saxsAnalyzer
import json
from nvd3 import lineWithFocusChart
from nvd3 import lineChart
app = Flask(__name__)


@app.route("/test")
def indextest():
    chart = lineWithFocusChart(show_labels=False, name='lineWithFocusChart', x_is_date=True, x_axis_format="%d %b %Y")
    chart.show_legend(False)
    xdata = [1365026400000000, 1365026500000000, 1365026600000000,
             1365026700000000, 1365026800000000, 1365026900000000, 1365027000000000]
    ydata = [-6, 5, -1, 2, 4, 8, 10]

    extra_serie = {"tooltip": {"y_start": "", "y_end": " ext"},
                       "date_format": "%d %b %Y"}
    chart.add_serie(name="Serie 1", y=ydata, x=xdata, extra=extra_serie)
    chart.buildhtml()
    return chart.htmlcontent

@app.route("/")
def index():
    chart = lineWithFocusChart(name='lineWithFocusChart')
    #chart = lineChart(name='lineChart')
    data = saxsAnalyzer.getdata()
    for index,saxsdata in enumerate(data):
    	if index < 5 :
    		chart.add_serie(name="Serie " + str(index), y=saxsdata[1], x=saxsdata[0])
    chart.buildhtml()
    return chart.htmlcontent

@app.route("/saxs")
def circlegathering():
    data = saxsAnalyzer.getdata()
    alldata = []
    for saxsdata in data:
        alldata.append(saxsdata[1].tolist())
    json_data = json.dumps(alldata)
    return json_data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
