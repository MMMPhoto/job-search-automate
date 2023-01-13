#! /usr/bin/env python3

import re

# Search for 'year(s)', with number preceding
def yearsSearch(text):
    yearsExperienceRegex = re.compile(r'''
        \d(?:-?\d)?      # number of years (account for range)
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

# Below is test code to tweak regex
text = "Description:\nNational HME is the one of the nation's largest direct service durable medical equipment providers offering services from more than 50 full service branch locations and additional network providers. Do you have a heart for helping people? Are you looking for a rewarding work opportunity? If so, please consider applying to join our team at National HME! We are looking for compassionate individuals who want to make a difference in our patients' lives. National HME, Inc. is now accepting applications for positions working at our location in Marietta, GA .\n \nWe have an immediate need for a full time Medical Service Technician Driver . We offer a competitive hourly rate, full benefits, 401k with match, PTO, and training in career path. MST's deliver and instruct hospice patients or family members on medical equipment and supplies in their place of residence or assisted care facility while providing highly responsible patient care services in addition to the following responsibilities.\n Safely drive and maintain company vehicle (16-foot box truck or van).Receives a daily route and required supply list and prepares the truck for delivery by pulling stock, loading equipment on the truck, and securing and staging the vehicle.Delivers, unloads, and sets the equipment to full functionality.Reviews basic equipment operation and instructs patients and/or caregivers on the proper use and care.Follows the daily route to pick up and/or exchange equipment. Breaks down, loads and returns equipment.Effectively communicates with customer service to relay order changes and issues, route delays, stock availability and delivery and pick up of equipment.Champions our Mission Statement and Family Standard and filter decisions through them.\nRequirements:High school diploma or general education degree (GED) requiredDelivery experience preferredA current state issued driver's license is requiredAbility to pass a motor vehicle records check (MVR) having it show no major violations (including DUI) in the past 5 consecutive years.Must be at least 21 years of age.Experience working in healthcare, home health or the medical field, preferredMust demonstrate practical knowledge of cleaning techniques and processes applicable to the industry.Applicant must have a clean state criminal background and federal sex offender check, clean drug test, valid driver's license and pass a driving skill test.Available for on-call assignments as needed.Applicant must demonstrate good organization, time management, and communication skills.Must demonstrate proficient ability to foster professional working relationships utilizing strong interpersonal and communication skills organization-wide.Requires the ability to safely operate a company vehicleRequires stamina to maintain attention to detail despite interruptionsRequires strength to lift and carry machinery and/or equipment weighing up to 100 poundsRequires sitting, walking, standing, talking or listeningRequires close vision to small print on computer and or paperwork and our electronic tablet\n\n \nNational HME is an equal opportunity employer that is committed to diversity and inclusion in the workplace. We prohibit discrimination and harassment of any kind based on race, color, sex, religion, sexual orientation, national origin, disability, genetic information, pregnancy, or any other protected characteristic as outlined by federal, state, or local laws.\n \nThis policy applies to all employment practices within our organization, including hiring, recruiting, promotion, termination, layoff, recall, leave of absence, compensation, benefits, and training. National HME makes hiring decisions based solely on qualifications, merit, and business needs at the time.\n \nEvery day, our team members make an impact on the lives of others within their communities. They are compassionate, caring, and friendly and provide comfort to those in hospice care. You will go home every day knowing that you made someone's life better. If you are looking for work with a purpose, come join our growing team and make a difference!"
years = yearsSearch(text)
context = yearsContextSearch(text)
skills = skillsSearch(text)

print(years)
print(context)
print(skills)

# Things to improve Regex:
    # 'aws' in skills pulls random letters from other words
    # mention of ages like '18 years old' or '21 years old' get flagged - exclude above a certain number?
