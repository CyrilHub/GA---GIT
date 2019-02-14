from flask import Flask, render_template
import requests

app = Flask(__name__)



#given a csv, load into dictionary called database
def loadDictionary(filename):
    database = {}

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line=0
        for row in csv_reader:
            if line == 0:
                pass
            else:
                username = row[0]
                ticker = row[1]
                if username in database.keys():
                    database[username]["tickers"].append(ticker)
                else:
                    database[username] = {
                        "tickers": [ticker]
                    }


def fetchCompany(ticker):
    # GET request to url www.iextrading.com/company_name
    # format is for python telling the ticker in the 
    r = requests.get("https://api.iextrading.com/1.0/stock/{}/book".format(ticker))
    # if r.json() == {}:
    #     name = "COMPANY NOT FOUND"
    #     market_cap = "?"
    #     return ({"name": name, "market_cap":market_cap, "ticker":ticker})
    name = r.json()["quote"]["companyName"]
    market_cap = r.json()["quote"]["marketCap"]
    # returning a dictionare
    return({
        "name": name,
        "market_cap": market_cap,
        "ticker": ticker
    })

    # parse request into databse
    #

@app.route('/')
def home():
    return render_template('home.html')



@app.route("/<user_ticker>")
def company(user_ticker):
    # the is to pass the keyword
    return render_template("company.html", x=fetchCompany(user_ticker))



# Run the app when the program starts!
if __name__ == '__main__':
    app.run(debug=True)
    # fetchCompany("goog")
