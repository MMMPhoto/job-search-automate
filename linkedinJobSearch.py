#! /usr/bin/env python3

# Import modules
import os, pprint, json
from linkedin_api import Linkedin
from dotenv import load_dotenv

# Handle environment variables
load_dotenv()
user = os.getenv('LINKEDIN_USERNAME')
pw = os.getenv('LINKEDIN_PW')

# Autheniticate Linkedin account
api = Linkedin(user, pw)

# Search jobs
jobResults = api.search_jobs(
    keywords='software developer',
    location_name='Atlanta, Georgia, United States',
    limit=10
)

pprint.pp(jobResults)
# Iterate search results to get full job data by ID
fullJobResults = []

for i in range(len(jobResults) - 1):
    jobId = jobResults[i].get('dashEntityUrn').removeprefix('urn:li:fsd_jobPosting:') # get the value holding job number (and remove extraneous prefix)
    job = api.get_job(jobId) # search for job by ID

    # Create new dictionary with only necessary data
    basicJob = {}
    basicJob['jobId'] = jobId
    basicJob['title'] = job['title']
    basicJob['company'] = job['companyDetails']['com.linkedin.voyager.deco.jobs.web.shared.WebCompactJobPostingCompany']['companyResolutionResult']['name']
    basicJob['description'] = job['description']['text']
    basicJob['listedAt'] = job['listedAt']

    fullJobResults.append(basicJob) # add to list

# pprint.pp(fullJobResults)
jobFile = open('./jobTestFile.json', 'w')
jobFile.write(json.dumps(fullJobResults))