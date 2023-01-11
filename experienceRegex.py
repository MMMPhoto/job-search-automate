#! /usr/bin/env python3

import re, pyperclip

# Regex for years of experience on job posting
# Search for 'year(s)', with number preceding
yearsExperienceRegex = re.compile(r'''
    \d(?:-\d)?      # number of years (account for range)
    \+?             # with a plus (optional)
    \syear(?:s)?    # years with space before
''', re.VERBOSE)

# Search for 'year(s), with context characters before and after
yearsContextRegex = re.compile(r'''
    .{0,20}         # Get 10 characters before match
    \syear(?:s)?    # years with space before
    .{0,100}         # Get 30 characters after match
''', re.VERBOSE)

# Get text off of clipboard
textTest = pyperclip.paste()


yearsExperience = yearsExperienceRegex.findall(textTest)
yearsContext = yearsContextRegex.findall(textTest)
print(f'Years experience: {yearsExperience}')
print(f'Years context: {yearsContext}')