from bs4 import BeautifulSoup
import requests
import re

url = "http://localhost/page1.html"

ret = requests.get(url)
txt = ret.content.decode("utf-8")
soup = BeautifulSoup(txt, features = "html.parser")

jpg = re.compile(".jpg")

a = soup.find_all("a", { "href": jpg })

count = 1

for b in a:

	c = "http://localhost/{}".format(b.attrs["href"])

	img = requests.get(c)

	fileName = "img/{}.jpg".format(count)

	imgFile = open(fileName, "wb")
	
	imgFile.write(img.content)

	imgFile.close()

	print("{} done!".format(fileName))

	count += 1

