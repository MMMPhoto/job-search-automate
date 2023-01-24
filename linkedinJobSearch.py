#! /usr/bin/env python3

# Import modules
import os, pprint, json, pygsheets
import pandas as pd
from linkedin_api import Linkedin
from dotenv import load_dotenv
from experienceRegex import yearsSearch, yearsContextSearch, skillsSearch

# Handle environment variables
load_dotenv()
user = os.getenv('LINKEDIN_USERNAME')
pw = os.getenv('LINKEDIN_PW')
gc = pygsheets.authorize(service_file='./job-search-service.json')

# Test data to dataframe
with open('./jobTestFile.json', 'r') as file:
  savedJobs = json.load(file)
pprint.pp(savedJobs)

# Create Dataframe
df = pd.DataFrame(savedJobs)

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


# # Write to google drive test:

# # Create a column
# df['name'] = ['John', 'Steve', 'Sarah']

#Open google spreadsheet (string parameter is name of sheet)
sh = gc.open('Automated Job Search')

#select the first sheet 
wks = sh[0]

#update the first sheet with df, starting at cell B2. 
wks.set_dataframe(df,(1,1))
