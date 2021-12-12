import requests

def fetch_api(q):
  base_url = "http://challenge-server.code-check.io"
  endpoint = "/api/hash"
  url = base_url + endpoint
  params= {
    "q":q,
  }
  res = requests.get(url, params = params)
  print(res.json()["hash"])

fetch_api("fizbuzz")
