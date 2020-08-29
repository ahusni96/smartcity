from bs4 import BeautifulSoup
import requests

url = "http://localhost/index.html"

ret = requests.get(url)
txt = ret.content.decode("utf-8")

soup = BeautifulSoup(txt, features = "html.parser")

print(soup.find("h1"))

a = soup.find_all("h2")

for b in a:
    print(b)

c = soup.find_all("a")

for d in c:
    e = d.get_text()
    f = d.attrs["href"]
    print("{} : {}".format(e, f))