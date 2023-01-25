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
existingIds = wks.get_col(1, include_tailing_empty=False) # Get job numbers in column 1
numRowsExisting = len(existingIds)
del existingIds[0]

# Search new jobs
searchResults = api.search_jobs(
  keywords='software developer',
  location_name='Atlanta, Georgia, United States',
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
    jobClean['Date Added'] = dt.datetime.now().date()
    jobClean['Job Id'] = jobId
    jobClean['Url'] = f'https://www.linkedin.com/jobs/view/{jobId}/'
    jobClean['Job Title'] = job['title']
    jobClean['Company'] = job['companyDetails']['com.linkedin.voyager.deco.jobs.web.shared.WebCompactJobPostingCompany']['companyResolutionResult']['name']
    jobClean['Description'] = job['description']['text']
    jobClean['Years Experience'] = yearsSearch(job['description']['text'])
    jobClean['Years Context'] = yearsContextSearch(job['description']['text'])
    jobClean['Skills'] = skillsSearch(job['description']['text'])

    newJobs.append(jobClean) # add to list

    # Format years experience
    jobClean['years experience'] = '\n'.join(jobClean['years experience'])

    # Format years context
    contextList = jobClean['years context']
    contextFormat = []
    for context in contextList:
      contextFormat.append(f'....{context}....')
    jobClean['years context'] = '\n'.join(contextFormat)

    # Format skills
    skills = jobClean['skills']
    skillsTemp = []
    skillsCount = []
    for skill in skills:
      if skill not in skillsTemp:
        skillsTemp.append(skill)
        count = skills.count(skill)
        skillsCount.append(f'{skill}({count})')
    jobClean['skills'] = '\n'.join(skillsCount)

# pprint.pp(newJobs)

# # Write to JSON file
# jobFile = open('./jobTestFile.json', 'w')
# jobFile.write(json.dumps(fullJobResults))

# Write to google drive:
# Create Dataframe
df = pd.DataFrame(jobs)

#update the first sheet with df, starting at cell B2
# wks.set_dataframe(df,(2,1), copy_head=False)
wks.set_dataframe(df, ((numRowsExisting + 1),1), copy_head=False, extend=True) # set dataframe to sheet on first empty row
