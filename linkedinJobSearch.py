#! /usr/bin/env python3

# Import modules
import os, pprint, json, pygsheets
import pandas as pd
import datetime as dt
from linkedin_api import Linkedin
from dotenv import load_dotenv
from experienceRegex import yearsSearch, yearsContextSearch, skillsSearch

# Handle environment variables
load_dotenv()
user = os.getenv('LINKEDIN_USERNAME')
pw = os.getenv('LINKEDIN_PW')
googleSheets = pygsheets.authorize(service_file='./job-search-service.json')

# Test data to dataframe
with open('./jobTestFile.json', 'r') as file:
  jobs = json.load(file)
# pprint.pp(jobs)

# # Autheniticate Linkedin account
# api = Linkedin(user, pw)

# # Search jobs
# jobResults = api.search_jobs(
#     keywords='software developer',
#     location_name='Atlanta, Georgia, United States',
#     limit=10
# )

# # Print to console (test variable)
# # pprint.pp(jobResults)

# # Iterate search results to get full job data by ID
# fullJobResults = []
# for i in range(len(jobResults) - 1):
#     jobId = jobResults[i].get('dashEntityUrn').removeprefix('urn:li:fsd_jobPosting:') # get the value holding job number (and remove extraneous prefix)
#     job = api.get_job(jobId) # search for job by ID

#     # Create new dictionary with only necessary data
#     basicJob = {}
#     basicJob['Job Id'] = jobId
#     basicJob['Job Title'] = job['title']
#     basicJob['Company'] = job['companyDetails']['com.linkedin.voyager.deco.jobs.web.shared.WebCompactJobPostingCompany']['companyResolutionResult']['name']
#     basicJob['Description'] = job['description']['text']
#     basicJob['Years Experience'] = yearsSearch(job['description']['text'])
#     basicJob['Years Context'] = yearsContextSearch(job['description']['text'])
#     basicJob['Skills'] = skillsSearch(job['description']['text'])

#     fullJobResults.append(basicJob) # add to list

# Print to console (test variable)
# pprint.pp(fullJobResults)


# # Write to JSON file
# jobFile = open('./jobTestFile.json', 'w')
# jobFile.write(json.dumps(fullJobResults))

#Open google spreadsheet, get 
sheet = googleSheets.open('Automated Job Search')
wks = sheet[0]
existingIds = wks.get_col(1, include_tailing_empty=False) # Get job numbers in column 1
# del existingIds[0]

# Clean up data
for job in jobs:
  # Remove job if already in spreadsheet
  if job['jobId'] in existingIds:
    jobs.remove(job)
  # pprint.pp(jobs)

  # Add URL
  id = job['jobId']
  job['url'] = f'https://www.linkedin.com/jobs/view/{id}/'

  # Add current date
  dateAdded = dt.datetime.now().date()
  job['Date Added'] = dateAdded

  # Reorder lists as strings
  job['years experience'] = '\n'.join(job['years experience'])
  job['years context'] = '\n'.join(job['years context'])
  job['skills'] = '\n'.join(job['skills'])

# Write to google drive:
# Create Dataframe
df = pd.DataFrame(jobs)

#update the first sheet with df, starting at cell B2
# wks.set_dataframe(df,(2,1), copy_head=False)
wks.set_dataframe(df,(1,1))
