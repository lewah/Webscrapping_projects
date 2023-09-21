# import requests
from serpapi import GoogleSearch

params = {
  "api_key": "4cdbae9173201ce90914fb8f6e154aba1304926a33d26e5c90a38e724d53957d",
  "engine": "google_jobs",
  "google_domain": "google.com",
  "q": "Data Science"
}
# test if connection is successful 
# try:
#     search = GoogleSearch(params)
#     results = search.get_dict()

#     if search.status_code == 200:
#         print("Connection successful")
#     else:
#         print("Connection failed with status code:", search.status_code)

# except Exception as e:
#     print("An error occurred:", str(e))


search = GoogleSearch(params)
results = search.get_dict()

# Access job results
job_results = results.get("jobs_results", [])

# Check if there are job results
if job_results:
    for job in job_results:
        # print (job)
        # Access individual job data
        job_title = job.get("title", "")
        company = job.get("company_name", "")
        location = job.get("location", "")
        via = job.get("via","")
        time = job.get ("detected_extensions","")
        # description = job.get("description", "")
        
        # Print job details
        print(f"Job Title: {job_title}")
        print(f"Company: {company}")
        print(f"Location: {location}")
        print(f"Via: {via}")
        print(f"Posted and Duration: {time}")
        # print(f"Description: {description}")
        print("\n")
else:
    print("No job results found.")