import urllib.request
import json
import ssl

url = "https://marketscout-dnp8.onrender.com/api/auth/register"
data = json.dumps({"name": "test", "email": "test12345@gmail.com", "password": "password"}).encode("utf-8")
headers = {"Content-Type": "application/json"}
req = urllib.request.Request(url, data=data, headers=headers, method="POST")
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    with urllib.request.urlopen(req, context=ctx) as response:
        print("STATUS:", response.status)
        print(response.read().decode("utf-8"))
except urllib.error.HTTPError as e:
    print("HTTP ERROR:", e.code)
    print(e.read().decode("utf-8"))
except Exception as e:
    print("ERROR:", e)
