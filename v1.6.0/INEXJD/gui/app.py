import os
import sys
from flask import Flask, render_template, jsonify, request
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import INEXJD
from INEXJD.SQL.getTables import getTables
from INEXJD.SQL.getTableData import getTableData
from INEXJD.SQL.query_parser import execute_query

app = Flask(__name__)
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
app.template_folder = template_dir


@app.route("/")
def index():
    tables = getTables().get("tables", {})
    return render_template("index.html", tables=tables, version=INEXJD.__version__)


@app.route("/api/tables")
def api_tables():
    return jsonify(getTables())


@app.route("/api/table/<table_name>")
def api_table(table_name):
    try:
        return jsonify({"data": getTableData(table_name)})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/api/query", methods=["POST"])
def api_query():
    try:
        query = request.json.get("query", "")
        results = execute_query(query)
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)})


def run_gui(host="127.0.0.1", port=5000, debug=False):
    app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    run_gui()
