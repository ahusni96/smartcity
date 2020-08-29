import re

file = open("file.txt", "r")

text = file.read()

res = re.findall("far", text)

print(len(res))