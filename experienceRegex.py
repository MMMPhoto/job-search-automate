#! /usr/bin/env python3

import re

# Search for 'year(s)', with number preceding
def yearsSearch(text):
    yearsExperienceRegex = re.compile(r'''
        \d(?:-\d)?      # number of years (account for range)
        \+?             # with a plus (optional)
        \syear(?:s)?    # years with space before
    ''', re.VERBOSE)
    return yearsExperienceRegex.findall(text)

# Search for 'year(s), with context characters before and after
def yearsContextSearch(text):
    yearsContextRegex = re.compile(r'''
        .{0,20}         # Get 20 characters before match
        \syear(?:s)?    # years with space before
        .{0,100}         # Get 100 characters after match
    ''', re.VERBOSE)
    return yearsContextRegex.findall(text)

# Search for list of skills
def skillsSearch(text):
    skillsRegex = re.compile(r'''
        (   # List skills found in job posting
            front(?:\s|-)?end               |
            full(?:\s|-)?stack              |
            java(?:\s|-)?script(?:es6+)?    |
            html(?:5)?                      |
            css(?:3)?                       |
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
    return skillsRegex.findall(text)