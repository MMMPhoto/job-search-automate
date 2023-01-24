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
pprint.pp(jobs)

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
#     basicJob['jobId'] = jobId
#     basicJob['title'] = job['title']
#     basicJob['company'] = job['companyDetails']['com.linkedin.voyager.deco.jobs.web.shared.WebCompactJobPostingCompany']['companyResolutionResult']['name']
#     basicJob['description'] = job['description']['text']
#     basicJob['years experience'] = yearsSearch(job['description']['text'])
#     basicJob['years context'] = yearsContextSearch(job['description']['text'])
#     basicJob['skills'] = skillsSearch(job['description']['text'])
#     basicJob['listedAt'] = job['listedAt']

#     fullJobResults.append(basicJob) # add to list

# Print to console (test variable)
# pprint.pp(fullJobResults)



# jobFile = open('./jobTestFile.json', 'w')
# jobFile.write(json.dumps(fullJobResults))

# Clean up data
for job in jobs:
  # Add URL
  id = job['jobId']
  print(id)
  job['url'] = f'https://www.linkedin.com/jobs/view/{id}/'

  # Clean up date
  # secs = job['listedAt'] % 86400
  # days = job['listedAt'] / 86400
  # print(days)

  print(dt.datetime.now())


# Write to google drive:
# Create Dataframe
df = pd.DataFrame(jobs)

#Open google spreadsheet, get 
sheet = googleSheets.open('Automated Job Search')
wks = sheet[0]
listIds = wks.get_col(1)
print(listIds)

#update the first sheet with df, starting at cell B2. 
# wks.set_dataframe(df,(1,1))
