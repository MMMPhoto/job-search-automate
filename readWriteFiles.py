#! /usr/bin/env python3

# Import modules
import os, pprint, json, pygsheets
import pandas as pd
from dotenv import load_dotenv

# Handle environment variables, authentication
load_dotenv()
localJson = os.getenv('local_JSON_file')
googleSheetsFile = os.getenv('google_sheets_file')
googleSheets = pygsheets.authorize(service_file='./job-search-service.json')

# Open local JSON 
def readFromJson():
  fileSize = os.stat(f'./{localJson}').st_size
  if fileSize != 0: 
    with open(f'./{localJson}', 'r') as file:
      jobsInJson = json.load(file)
  else:
    jobsInJson = []
  # pprint.pp(jobsInJson)
  print(f'Opened local Json document, found {len(jobsInJson)} jobs...')
  return jobsInJson


#Open google spreadsheet, get existing job IDs
def readFromSheets():
  sheet = googleSheets.open(googleSheetsFile)
  wks = sheet[0]
  existingIds = wks.get_col(3, include_tailing_empty=False) # Get job numbers in column 1
  numRowsExisting = len(existingIds)
  del existingIds[0]
  print(f'Opened google sheet, found {len(existingIds)} jobs...')
  return wks, existingIds, numRowsExisting


# Write to JSON file
def writeToJson(jobsInJson):
  if len(jobsInJson) != 0:
    with open(f'./{localJson}', 'w') as newFile:
      newFile.write(json.dumps(jobsInJson))
      newFile.close()
    print(f'Wrote {len(jobsInJson)} total jobs back to local JSON file!')
  else:
    print('There were no jobs to write to local JSON file!')
  return

# Write to google drive:
def writeToGoogleDrive(newJobs, wks, numRowsExisting):
  if len(newJobs) != 0:    
    df = pd.DataFrame(newJobs) # create dataframe
    wks.set_dataframe(df, ((numRowsExisting + 1),2), copy_head=False, extend=True) # set dataframe to sheet on first empty row
    print(f'Wrote {len(newJobs)} new jobs to google sheet!')
  else:
    print('There were no new jobs to write to google sheet!')
  return
