#! /usr/bin/env python3

# Import modules
import os, pprint, json, pygsheets
import pandas as pd
import datetime as dt
from linkedin_api import Linkedin
from dotenv import load_dotenv
from experienceRegex import yearsSearch, yearsContextSearch, skillsSearch

# Handle environment variables, authentication
load_dotenv()
user = os.getenv('LINKEDIN_USERNAME')
pw = os.getenv('LINKEDIN_PW')
googleSheets = pygsheets.authorize(service_file='./job-search-service.json')

# Autheniticate Linkedin account
api = Linkedin(user, pw)

# Open local JSON file
fileSize = os.stat('./jobSearchData.json').st_size
if fileSize != 0: 
  with open('./jobSearchData.json', 'r') as file:
    jobsInJson = json.load(file)
else:
  jobsInJson = []
# pprint.pp(jobsInJson)

#Open google spreadsheet, get existing job IDs
sheet = googleSheets.open('Automated Job Search')
wks = sheet[0]
existingIds = wks.get_col(3, include_tailing_empty=False) # Get job numbers in column 1
numRowsExisting = len(existingIds)
del existingIds[0]

# Search new jobs
searchResults = api.search_jobs(
  keywords='software developer',
  location_name='Atlanta, Georgia, United States',
  distance=3000,
  remote=True,
  limit=10
)
# pprint.pp(searchResults)

# Iterate search results to get full job data by ID
newJobs = []
for result in searchResults:
  jobId = result.get('dashEntityUrn').removeprefix('urn:li:fsd_jobPosting:') # get the value holding job number (and remove extraneous prefix)
  
  # Check to make sure job is not in existing spreadsheet
  if jobId not in existingIds:

    job = api.get_job(jobId) # search for job by ID
      
    # Create new dictionary with only necessary data
    jobClean = {}
    jobClean['Date Added'] = dt.datetime.now().date().strftime('%m/%d/%Y')
    jobClean['Job ID'] = jobId
    jobClean['URL'] = f'https://www.linkedin.com/jobs/view/{jobId}/'
    jobClean['Job Title'] = job['title']
    jobClean['Company'] = job['companyDetails']['com.linkedin.voyager.deco.jobs.web.shared.WebCompactJobPostingCompany']['companyResolutionResult']['name']
    jobClean['Description'] = job['description']['text']
    jobClean['Years Experience'] = yearsSearch(job['description']['text'])
    jobClean['Years Context'] = yearsContextSearch(job['description']['text'])
    jobClean['Skills'] = skillsSearch(job['description']['text'])
    jobClean['Remote Allowed'] = job['workRemoteAllowed']

    jobsInJson.append(jobClean) # add to JSON job list

    # Format years experience
    jobClean['Years Experience'] = '\n'.join(jobClean['Years Experience'])

    # Format years context
    contextList = jobClean['Years Context']
    contextFormat = []
    for context in contextList:
      contextFormat.append(f'....{context}....')
    jobClean['Years Context'] = '\n'.join(contextFormat)

    # Format skills
    skills = jobClean['Skills']
    skillsTemp = []
    skillsCount = []
    for skill in skills:
      if skill not in skillsTemp:
        skillsTemp.append(skill)
        count = skills.count(skill)
        skillsCount.append(f'{skill}({count})')
    jobClean['Skills'] = '\n'.join(skillsCount)

    newJobs.append(jobClean) # add to new jobs list for sheets

pprint.pp(jobsInJson)
pprint.pp(f'new jobs: {newJobs}')

# Write to JSON file
with open('./jobSearchData.json', 'w') as newFile:
  newFile.write(json.dumps(jobsInJson))
  newFile.close()
print('Wrote new jobs data to local JSON file')

# Write to google drive:
df = pd.DataFrame(newJobs) # create dataframe
wks.set_dataframe(df, ((numRowsExisting + 1),2), copy_head=False, extend=True) # set dataframe to sheet on first empty row
print('Wrote new jobs data to google sheet')
