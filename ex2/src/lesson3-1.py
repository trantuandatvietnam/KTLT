import requests

logins = []

with open("D:\Work Space\Python\ex2\src\login.txt", "r") as filehandler:
    for line in filehandler:
        # Remove all \n of each line 
        login = line[:-1]
        logins.append(login)

domain = "http://qldt.actvn.edu.vn"
subDomain = "/CMCSoft.IU.Web.info"

for login in logins:
    print("Checking..." + domain + subDomain +  login)
    response = requests.get(domain + subDomain + login )
    print(response)
    if response.status_code == 200:
        print("Login resource detected: " + login)
        break