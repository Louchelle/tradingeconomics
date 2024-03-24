from flask import Flask, render_template
from tabulate import tabulate
import requests

app = Flask(__name__)

api_key = 'df165f878fb6485:x2q6mahbydl6z2o'
url = f'https://api.tradingeconomics.com/country/mexico?c={api_key}'

data = requests.get(url).json()

formatted_table = tabulate(data, tablefmt='html')


@app.route("/")
def index():
  return render_template('index.html')


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)
