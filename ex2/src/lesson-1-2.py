from dotenv import load_dotenv
import shodan
import os
# Load all env vars
load_dotenv()

servers = []

SHODAN_API_KEY = os.environ['API_SHODAN']
shodanApi = shodan.Shodan(SHODAN_API_KEY)

results = shodanApi.search("port: 21 Anonymous user logged in")

print("hostnumber: " + str(len(results["matches"])))

for result in results["matches"]:
    if result['ip_str'] is not None:
        servers.append(result['ip_str'])
for server in servers:
    print(server)