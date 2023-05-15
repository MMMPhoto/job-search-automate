#! /usr/bin/env python3

# Import modules
import os, pprint, json, pygsheets
import datetime as dt
from linkedin_api import Linkedin
from dotenv import load_dotenv
from experienceRegex import yearsSearch, yearsContextSearch, skillsSearch

# Handle environment variables
load_dotenv()
user = os.getenv('LINKEDIN_USERNAME')
pw = os.getenv('LINKEDIN_PW')

# Autheniticate Linkedin account
api = Linkedin(user, pw)

# Search jobs by given parameters
def linkedinJobSearch(searchKeywords, location, radius, remoteOption, resultsNumber):
  print('Starting job search...')

  # Search new jobs
  searchResults = api.search_jobs(
    keywords=searchKeywords,
    location_name=location,
    distance=radius,
    remote=remoteOption,
    listed_at=604800, # 604800 == Past 7 days. Using default value (24 hrs) means result is less accurate for some reason
    limit=resultsNumber
  )
  print(f'Received {len(searchResults)} search results!')
  return searchResults

# Iterate search results to get full job data by ID
def sortJobResults(searchList, existingIds, jobsInJson):
  print('Cleaning up search results...')
  newJobs = []
  for result in searchList:
    jobId = result.get('dashEntityUrn').removeprefix('urn:li:fsd_jobPosting:') # get the value holding job number (and remove extraneous prefix)
    
    # Check to make sure job is not in existing spreadsheet
    if jobId not in existingIds:

      job = api.get_job(jobId) # search for job by ID

      # Create new dictionary
      jobClean = {}

      # Clean up time
      now = dt.datetime.now()
      rawTime = job.get('listedAt') / 1000
      jobTime = dt.datetime.fromtimestamp(rawTime)
      jobClean['Listed At'] = str(jobTime)
      
      # Clean up other data
      jobClean['Job ID'] = jobId
      jobClean['URL'] = f'https://www.linkedin.com/jobs/view/{jobId}/'
      jobClean['Job Title'] = job.get('title')
      jobClean['Company'] = job.get('companyDetails', {}).get('com.linkedin.voyager.deco.jobs.web.shared.WebCompactJobPostingCompany', {}).get('companyResolutionResult', {}).get('name')
      jobClean['Remote Allowed'] = job.get('workRemoteAllowed')
      jobClean['Description'] = job.get('description', {}).get('text')
      jobClean['Years Experience'] = yearsSearch(jobClean['Description'])
      jobClean['Years Context'] = yearsContextSearch(jobClean['Description'])
      jobClean['Skills'] = skillsSearch(jobClean['Description'])

      print(jobClean['Years Experience'])

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
      print(f'Cleaned up {len(newJobs)} new jobs...')

  # pprint.pp(jobsInJson)
  # pprint.pp(f'new jobs: {newJobs}')  
  print('Finished cleaning up search results...')
  return jobsInJson, newJobs
