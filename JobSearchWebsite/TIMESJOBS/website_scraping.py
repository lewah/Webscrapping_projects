# If you want to scrap a website 
# website - https://www.timesjobs.com/candidate/contact.html

from bs4 import BeautifulSoup
import requests

# import sys
# print(sys.executable)

web_link = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analysis&txtLocation=Germany')
html_file = web_link.text
# print(html_file) - check if you can fetch 
soup = BeautifulSoup(html_file, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

# 1
# jobs = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
# # print(jobs)
# company_nmae =soup.find('h3', class_ = 'joblist-comp-name').text
# # print(company_nmae)

# 2 
# jobs = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
# company_name =jobs.find('h3', class_ = 'joblist-comp-name').text
# skills = jobs.find('span' , class_ = 'srp-skills').text
# posted_duration = jobs.find('span', class_ = 'sim-posted').span.text
# print(posted_duration)

# 3
# for job in jobs:
#     # jobs = job.find('li', class_ = 'clearfix job-bx wht-shd-bx')
#     company_name =job.find('h3', class_ = 'joblist-comp-name').text
#     skills = job.find('span' , class_ = 'srp-skills').text
#     posted_duration = job.find('span', class_ = 'sim-posted').span.text

#     print(f'''
#     Company Name : {company_name} 
#     Skills : {skills} 
#     Date posted : {posted_duration} 
#     ''')

# 4 here we will filter posted_duration to posted a few days ago
for job in jobs:
    posted_duration = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in posted_duration:
        company_name =job.find('h3', class_ = 'joblist-comp-name').text
        skills = job.find('span' , class_ = 'srp-skills').text.replace(' ', '')
        job_link = job.header.h2.a['href']
        print(f"Company Name : {company_name.strip()} ")
        print(f"Skills : {skills.strip()} ")
        print(f"Date posted : {posted_duration.strip()} ")
        print(f" Link : {job_link} \n")
