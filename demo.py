#coding utf-8
import os
import urllib.request
import urllib.parse
import re

req=urllib.request.urlopen("http://www.quanmama.com/search/?keyword=%E9%A5%BF%E4%BA%86%E4%B9%88")
reqData=req.read().decode("utf-8")
# print(reqData)
pattern=re.compile(r"<a href=.*? title=\"饿了.*?>")

results=re.findall(pattern,reqData)
res=[]
for result in results:
    a=result.split(" ")
    b=a[1]
    b=b.split("=")
    res.append(b[1][1:-1])
print(res)


