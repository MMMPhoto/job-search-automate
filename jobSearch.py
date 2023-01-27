#! /usr/bin/env python3

# Import modules
# import os, pprint, json, pygsheets
# import pandas as pd
# import datetime as dt
# from linkedin_api import Linkedin
# from dotenv import load_dotenv
from readWriteFiles import readFromJson, readFromSheets, writeToJson, writeToGoogleDrive
from linkedinJobSearch import linkedinJobSearch, sortJobResults

# Search for new jobs by parameters
jobsInJson = readFromJson()
wks, existingIds, numRowsExisting = readFromSheets()
searchResults = linkedinJobSearch('software developer', 'Atlanta, Georgia, United States', 25, False, 10) # software developer non-remote Atlanta jobs, no limit
newJobsInJson, newJobs = sortJobResults(searchResults, existingIds, jobsInJson)
writeToJson(newJobsInJson)
writeToGoogleDrive(newJobs, wks, numRowsExisting)

# searchResults = linkedinJobSearch('software developer', 'Atlanta, Georgia, United States', 3000, True, -1) # software developer remote jobs, no limit
# newJobsInJson, newJobs = sortJobResults(searchResults, existingIds, jobsInJson)
