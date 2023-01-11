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
    .{0,20}         # Get 20 characters before match
    \syear(?:s)?    # years with space before
    .{0,100}         # Get 100 characters after match
''', re.VERBOSE)

# Search for list of skills
skillsRegex = re.compile(r'''
    (   # List skills found in job posting
        front(?:\s|-)?end               |
        full(?:\s|-)?stack              |
        java(?:\s|-)?script(?:es6+)?    |
        html                            |
        css                             |
        react(?:\s|-)?(?:native)?       |
        redux                           |
        node                            |
        express                         |
        python                          |
        (?:no|my)?sql                   |
        postgres                        |
        mongo                           |
        apollo                          |
        graphql                         |
        git                             |
        cypress                         |
        bootstrap                       |
        j(?:\s|-)?query                 |
        adobe                           |
        amazon                          |
        aws                             |
        java                            |
        python                          |
        ios                             |
        android                         |
        swift)
''', re.VERBOSE | re.IGNORECASE)

# Get text off of clipboard
textTest = pyperclip.paste()

yearsExperience = yearsExperienceRegex.findall(textTest)
yearsContext = yearsContextRegex.findall(textTest)
skillsList = skillsRegex.findall(textTest)

print(f'Years experience: {yearsExperience}')
print(f'Years context: {yearsContext}')
print(f'Skills listed: {skillsList}')