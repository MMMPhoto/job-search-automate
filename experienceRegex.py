#! /usr/bin/env python3

import re, pyperclip

# Regex for years of experience on job posting
# Search for 'years', with number preceding
yearsExperienceRegex = re.compile(r'''
    \d(?:-\d)?      # number of years (account for range)
    \+?             # with a plus (optional)
    \syear(?:s)?    # years with space before
''', re.VERBOSE)

# Get text off of clipboard
textTest = pyperclip.paste()

results = yearsExperienceRegex.findall(textTest)
print(results)