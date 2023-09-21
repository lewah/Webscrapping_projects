import requests
from bs4 import BeautifulSoup
import pandas as pd
# import json 



def exctract_data(page):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
               ,'Accept-Encoding':'gzip, deflate, br'
               ,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
               ,'Connection':'keep-alive'
               ,'Accept-Language':'en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6', }
    url = f'https://api.scrapingdog.com/scrape?api_key=6501b0f2e44b9a6b5577db79&url=https://www.indeed.com/jobs?q=data+scientist&l=Remote&start={page}'
    r = requests.get(url,headers) #get the URL first
    soup = BeautifulSoup(r.content,'html.parser')
    return soup

    # return r.status_code

def transform_data(soup):
    

    divs = soup.find_all('div', class_ = 'job_seen_beacon')
    # job_list = soup.find_all('li', class_ = 'css-5lfssm eu4oa1w0')
    for item in divs:
        title = item.find('a').text 
        company_name  = item.find('span', class_ = 'companyName').text
        company_loction = item.find('div', class_ = 'companyLocation').text
        try:
            salary = item.find('span', class_ = 'estimated-salary').text
            # salary = item.find('div', class_ = 'metadata salary-snippet-container').text   
        except:
            salary = ''
        try :
            duration = item.find('div', class_ = 'attribute_snippet').text #metadata
        except:
            duration = ''
        date_posted = item.find('span', class_ = 'date').text

        jobs = {
            'Title' : title,
            'Company' : company_name,
            'Location': company_loction,
            'Salary': salary,
            'Duration': duration,
            'PostingDate': date_posted
        }
        job_results.append(jobs)
        
        # print(title)  
    return 

# empty list to hold data from the function transform_data
job_results = [] 

# handling pagnation
for i in range(0,60,10):
    # here we are passing all the data in page 0 to the function exctract_data
    c = exctract_data(0)
    transform_data(c) # calling function

# create data frame for the data from job_results
df = pd.DataFrame(job_results)
# print(df.head())
df.to_csv('jobs.csv')
# print(exctract_data(10))
# print(transform_data(c))
# print(len(job_results))
# print(job_results)
