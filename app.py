from flask import Flask
from flask import render_template
import saxsAnalyzer
import json
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


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
