import requests

response = requests.get('https://serpapi.com/search.json?engine=google_jobs&q=Data+Science&google_domain=google.com&api_key=4cdbae9173201ce90914fb8f6e154aba1304926a33d26e5c90a38e724d53957d')
# print(response.status_code) -- statuse code is 200 this shows ists connecting 
print(response.json)