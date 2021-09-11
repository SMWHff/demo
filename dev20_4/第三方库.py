

import requests

r = requests.get("http://httpbin.org/get")
print(r.status_code)
print(r.text)

r = requests.post("http://httpbin.org/post", data={'key': 'value'})
print(r.status_code)
print(r.text)

