#! /usr/bin/env python3

import re, pyperclip

textTest = 'Looking for 7-8 years of experience'

# Regex for years of experience on job posting
# Search for 'years', with number preceding
yearsExperienceRegex = re.compile(r'''
    \d(?:-\d)?      # number of years (account for range)
    (?:\+)?         # with a plus (optional)
    (?:\syear(?:s)?)    # years with space before
''', re.VERBOSE)

results = yearsExperienceRegex.findall(textTest)
print(results)


