import config
import requests

# There is a time limit on the usage of token
# This code will let you generate a new one.

client_auth = requests.auth.HTTPBasicAuth(config.CLIENT_ID, config.CLIENT_SECRET)
post_data = {"grant_type": "password", "username": config.USERNAME, "password": config.PASSWORD}
headers = {"User-Agent": "Maverick/0.1 by twoweirdpeople"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
r=response.json()
print(r)

