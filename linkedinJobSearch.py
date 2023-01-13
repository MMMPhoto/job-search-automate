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
    experience=['2'],
    location_name='Atlanta, Georgia, United States',
    limit=10
)

# Iterate search results to get full job data by ID
fullJobResults = []

for i in range(len(jobResults) - 1):
    jobId = jobResults[i].get('dashEntityUrn').removeprefix('urn:li:fsd_jobPosting:') # get the value holding job number (and remove extraneous prefix)
    # pprint.pp(jobId)
    job = api.get_job(jobId) # search for job by ID
    # pprint.pp(job)
    fullJobResults.append(job) # add to list

# pprint.pp(fullJobResults)
jobFile = open('./jobTestFile.json', 'w')
jobFile.write(json.dumps(fullJobResults))

# # GET a profile
# profile = api.get_profile('billy-g')

# # GET a profiles contact info
# contact_info = api.get_profile_contact_info('billy-g')

# # GET 1st degree connections of a given profile
# connections = api.get_profile_connections('1234asc12304')




