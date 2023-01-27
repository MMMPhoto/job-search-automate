#! /usr/bin/env python3

from readWriteFiles import readFromJson, readFromSheets, writeToJson, writeToGoogleDrive
from linkedinJobSearch import linkedinJobSearch, sortJobResults

def readSearchWrite(searchKeywords, location, radius, remoteOption, resultsNumber):
  jobsInJson = readFromJson()
  wks, existingIds, numRowsExisting = readFromSheets()
  searchResults = linkedinJobSearch(searchKeywords, location, radius, remoteOption, resultsNumber)
  newJobsInJson, newJobs = sortJobResults(searchResults, existingIds, jobsInJson)
  writeToJson(newJobsInJson)
  writeToGoogleDrive(newJobs, wks, numRowsExisting)


# Run all searches
readSearchWrite('software developer', 'Atlanta, Georgia, United States', 25, False, -1) # software developer non-remote Atlanta jobs, no limit
readSearchWrite('software developer', 'Atlanta, Georgia, United States', 3000, True, -1) # software developer remote jobs, no limit
readSearchWrite('react developer', 'Atlanta, Georgia, United States', 25, False, -1) # react developer remote jobs, no limit
readSearchWrite('react developer', 'Atlanta, Georgia, United States', 3000, True, -1) # react developer remote jobs, no limit

print('Finished! Closing program.')
