from bs4 import BeautifulSoup
import requests
import pymysql #

con = pymysql.connect("localhost", "root", "root", "quotes") #
cur = con.cursor() #

url = "http://localhost/scarlet1.html"

ret = requests.get(url)
txt = ret.content.decode("utf-8")

soup = BeautifulSoup(txt, features = "html.parser")

a = soup.find_all("span")

sql = "INSERT INTO quotes (qTxt, qSpeaker) VALUES (%s, %s)"

for b in a:

	c = b.attrs["class"]
	d = b.get_text()

	if "watson" in c:
		cur.execute(sql, (d, 'Dr. Watson'))
		con.commit()
		print("Done!")