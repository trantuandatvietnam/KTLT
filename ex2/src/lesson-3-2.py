import requests

domain = "http://testphp.vulnweb.com/listproducts.php?cat="

mySplAttacks = []

with open("D:\Work Space\Python\ex2\src\mySql.txt") as hanlder:
    for line in hanlder:
       mySplAttacks.append(line[:-1])

for sql in mySplAttacks:
    try:
        reponse = requests.get(domain + sql + "&minify=True").json()
        print(reponse)
    except Exception as err:
        print(err)
