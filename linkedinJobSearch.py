#! /usr/bin/env python3

# Import modules
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
      print(f'Cleaned up {len(newJobs)} new jobs...')

  # pprint.pp(jobsInJson)
  # pprint.pp(f'new jobs: {newJobs}')  
  print('Finished cleaning up search results...')
  return jobsInJson, newJobs
