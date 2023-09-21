from serpapi import GoogleSearch
import json

params = {
  "api_key": "4cdbae9173201ce90914fb8f6e154aba1304926a33d26e5c90a38e724d53957d",
  "engine": "google_jobs",
  "google_domain": "google.com",
  "q": "Data Science",
  # 'hl': 'en',                 # language of the search
  # 'gl': 'us',                 # country of the search
	'start': 0									# pagination
}

google_jobs_results = [] # empty variable to hold job results

while True:
  search = GoogleSearch(params)   			# where data extraction happens on the SerpApi backend
  result_dict = search.get_dict() 			# Get the HTTP response(JSON data) as a Python dict

  if 'error' in result_dict:
    break
  
  # Accessing job results and appending it to google_jobs_results
  for result in result_dict['jobs_results']:  
    job_title = result.get("title", "")
    company = result.get("company_name", "")
    location = result.get("location", "")
    via = result.get("via","")
    time = result.get ("detected_extensions","")
    description = result.get("description", "")
    qualifications = result.get("items", "")
    extensions = result.get("extensions","")
    time_duration = result.get("detected_extensions","")

    # dict / data structure to hold data that will append to google_jobs_results
    job_data = {
        "job_title": job_title,
        "company": company,
        "location": location,
        "via": via,
        "time": time,
        "description": description,
        "qualifications": qualifications,
        "extensions": extensions,
        "time_duration": time_duration
    }

    google_jobs_results.append(job_data)
    # google_jobs_results.append(result)

  params['start'] += 4

# print(json.dumps(google_jobs_results, indent=2, ensure_ascii=False))
print (google_jobs_results)