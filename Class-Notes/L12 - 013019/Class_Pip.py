# Import Flask class from flask library. (Note the upper/lowercase convention.)
from flask import Flask

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

# The default URL ends in / ("my-website.com/").
# Could be instead "my-website.com/about" or anything - more on this later.
@app.route('/')
# Function that returns the page: Display "Hello, World!"
def index():
  return 'Hello, World!'

# Run the app when the program starts!
if __name__ == '__main__':
    app.run(debug=True)
