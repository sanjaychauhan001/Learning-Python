import requests as rq

data = rq.get("https://sanjaychauhan001.github.io/test1/java/prec1.txt").text
print(data)