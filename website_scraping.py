# If you want to scrap a website 
# website - https://www.timesjobs.com/candidate/contact.html

from bs4 import BeautifulSoup
import requests

# import sys
# print(sys.executable)

web_link = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analysis&txtLocation=Germany')
html_file = web_link.text
print(html_file)


