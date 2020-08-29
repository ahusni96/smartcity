import requests
import pymysql
import json

con = pymysql.connect("localhost", "root", "root", "exchange")
cur = con.cursor()

def insert(rate, date):
	sql = "INSERT INTO exchange (exRate, exDate) VALUES (%s, %s)"

	cur.execute(sql, (rate, date))
	con.commit()

def retrieve(limit):
	sql = "SELECT exRate, exDate FROM exchange ORDER BY exDate DESC LIMIT %s"

	cur.execute(sql, limit)
	rows = cur.fetchall()

	highest = 0
	lowest = 0

	for row in rows:
		#print(row)

		rate = float(row[0])

		if rate >= highest:
			highest = rate

		elif rate < highest and lowest == 0:
			lowest = rate

		elif rate < lowest and lowest != 0:
			lowest = rate

		else:
			rate = rate

	print("Highest: {} | Lowest: {}".format(highest, lowest))

function = "DIGITAL_CURRENCY_MONTHLY"
from_currency = "BTC"
to_currency = "USD"
apikey = "CUQHIJIHK8HP9DDK"

url = "https://www.alphavantage.co/query?function={}&symbol={}&market={}&apikey={}"
url = url.format(function, from_currency, to_currency, apikey)

res = requests.get(url)
res = res.text
res = json.loads(res)

monthly = res["Time Series (Digital Currency Monthly)"]
'''
for month in monthly:
	temp = monthly[month]

	insert(temp["4a. close (USD)"], month)
'''
retrieve(12)