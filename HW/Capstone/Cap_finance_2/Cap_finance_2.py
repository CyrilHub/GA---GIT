#project example 1

from flask import Flask, render_template
import requests
import csv

app = Flask(__name__)


held = {
       'dis' : 87.76,
       'nvda' : 19.62,
       'kopn' : 3.32,
       'calm' : 41.61,
       'cor' : 103.67,
       'grub' : 131.76,
       'kbr' : 20.79,
       'pcar' : 68.17,
       'shop' : 146.7,
       'swir' : 27.16,
       'ttwo' : 124.56,
       'xyl' : 67.25
       }

# watch = ['chrw', 'ddd', 'rop', 'mtch']
# sold = ['ba', 'hpq', 'agu']


#given a csv, load into dictionary called database


class StockCalcs:

   def __init__(self, ticker):
       self.tic = ticker

   def stock_return(self, purchase_price):

         





def fetchCompany(ticker):
   # GET request to url www.iextrading.com/company_name
   r = requests.get("https://api.iextrading.com/1.0/stock/{}/book".format(ticker))
   name = r.json()["quote"]["companyName"]
   market_cap = r.json()["quote"]["marketCap"]
   sector = r.json()["quote"]["sector"]
   current_price = r.json()["quote"]["latestPrice"]
   prev_close = r.json()["quote"]["previousClose"]
   purchase_price = held[ticker]


   return({
       "name": name,
       "market_cap": market_cap,
       "ticker": ticker,
       "sector": sector,
       "current_price": current_price,
       "prev_close": prev_close,
       "purchase_price": purchase_price
   })

   # parse request into databse



@app.route('/')
def home():
   return render_template('home.html')   #render template takes file from templates folder, then returns it as a string.

@app.route("/<user_ticker>" )
def company(user_ticker):

   return render_template("company.html", x=fetchCompany(user_ticker))

#
# with open('stocks_dis.csv', 'a', newline='') as csvfile:
#   # These are the header row values at the top.
#   fieldnames = ['purchase','target', 'current', 'date_time', 'change']
#   # This opens the `DictWriter`.
#   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#   # Write out the header row (this only needs to be done once!).
#   writer.writeheader()
#   # Write as many rows as you want!
#   for i in employees:
#     writer.writerow(i)

# fieldnames = ['purchase','target', 'current', 'date_time', 'change']
# with open('stocks_dis.csv','a',newline='') as f:
#     writer=csv.writer(f)
#     y = fetchCompany("dis")
#     writer.writerow([0,0,y["current_price"],0,0])

# with open('mycsvfile.csv') as f:
#     print(f.read())




# Run the app when the program starts!
if __name__ == '__main__':
   app.run(debug=True)
   # fetchCompany("goog")


# with open('stocks_dis.csv','a',newline='') as f:
#     writer=csv.writer(f)
#     y = fetchCompany("dis")
#     writer.writerow([0,0,y["current_price"],0,0])