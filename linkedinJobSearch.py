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

#Open google spreadsheet, get existing job IDs
sheet = googleSheets.open('Automated Job Search')
wks = sheet[0]
existingIds = wks.get_col(1, include_tailing_empty=False) # Get job numbers in column 1
numRowsExisting = len(existingIds)
del existingIds[0]

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

  # Format years experience
  job['years experience'] = '\n'.join(job['years experience'])

  # Format years context
  contextList = job['years context']
  contextFormat = []
  for context in contextList:
    contextFormat.append(f'....{context}....')
  job['years context'] = '\n'.join(contextFormat)

  # Format skills
  skills = job['skills']
  skillsTemp = []
  skillsCount = []
  for skill in skills:
    if skill not in skillsTemp:
      skillsTemp.append(skill)
      count = skills.count(skill)
      skillsCount.append(f'{skill}({count})')
  job['skills'] = '\n'.join(skillsCount)


# # Autheniticate Linkedin account
# api = Linkedin(user, pw)

# # Search new jobs
# searchResults = api.search_jobs(
#     keywords='software developer',
#     location_name='Atlanta, Georgia, United States',
#     limit=10
# )

# # Print to console (test variable)
# # pprint.pp(searchResults)

# # Iterate search results to get full job data by ID
# fullJobResults = []
# for i in range(len(searchResults) - 1):
#     jobId = searchResults[i].get('dashEntityUrn').removeprefix('urn:li:fsd_jobPosting:') # get the value holding job number (and remove extraneous prefix)
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

# Write to google drive:
# Create Dataframe
df = pd.DataFrame(jobs)

#update the first sheet with df, starting at cell B2
# wks.set_dataframe(df,(2,1), copy_head=False)
wks.set_dataframe(df, ((numRowsExisting + 1),1), copy_head=False, extend=True) # set dataframe to sheet on first empty row
