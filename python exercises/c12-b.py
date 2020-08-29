from bs4 import BeautifulSoup
import requests

url = "http://localhost/scarlet1.html"

ret = requests.get(url)
txt = ret.content.decode("utf-8")

soup = BeautifulSoup(txt, features = "html.parser")

a = soup.find_all("span")

for b in a:

	c = b.attrs["class"]
	d = b.get_text()

	if "watson" in c:
		print(d)
