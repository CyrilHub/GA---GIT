import requests
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def home():
    search_query = request.args.get("query")
    api = OMDBApi()
    results = api.list_search_result_request(search_query)
    print(results)
    return render_template("home.html", query=search_query, results=results)


if __name__ == "__main__":
    app.run(debug=True)