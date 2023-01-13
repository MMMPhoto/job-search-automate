#! /usr/bin/env python3

import re

# Search for 'year(s)', with number preceding
def yearsSearch(text):
    yearsExperienceRegex = re.compile(r'''
        \d(?:-?\d)?     # number of years (account for range)
        (?:!18|21)      # exclude 18 or 21
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
text = "Job Description\n\nRole Summary/Purpose:\n\nA Software Engineer Should Be Proficient In\n\nSoftware Engineers have extensive knowledge of programming languages, the environments in which software are developed and operated and are well versed in software development lifecycle. A software engineer can be front-end, back-end or full-stack engineers.\nProgramming and codingFundamentals of computer scienceDesign and architectureAlgorithms and data structuresInformation analysisDebugging softwareTesting softwareProficiency in integration patternsOutstanding all-round communication skills and ability to work collaboratively.\nWe\u2019re proud to offer you choice and flexibility. You have the option to be remote, and work from home, or come into one of our offices. You may be occasionally requested to commute to our nearest office for in person engagement activities such as team meetings, training and culture events.\n\nEssential Responsibilities\nDesign, develop and install software solutions to meet business and technical requirements.Work in a constantly evolving environment, due to technological advances and the strategic direction of the organization.Create, maintain, and audit software systems - built on high standards of availability, stability, security, and performance - in alignment with architects and analysts. Incorporate resiliency into software design and development.Investigate problem areas. Improve system quality by identifying issues and common patterns and developing standard operating procedures.Test software systems to diagnose and resolve system faults; Improve existing codebases and peer review code changes.Partner with technology leaders in adherence to technology strategy and roadmap.Follow software development lifecycle.Ensure that the software that is written is easy to integrate to, for internal and external consumption.Design and implement monitoring, alerting and appropriate metrics to track and report performance and operational efficiency of software.Research and recommend on evolving technologies, including mobile, Cloud and social media.Drive technical innovation and efficiency in software operations via simplification and automation.Create technical specifications and standards.Shared responsibility of supporting applications in productionPerform other duties and/or special projects as assigned\nQualifications/Requirements\nBachelor\u2019s degree and a minimum 5 years of experience with application development OR, in lieu of degree, High School Diploma/GED 7 years of application development experienceMinimum of 5 years of full stack development using Spring, other JEE technologies, Spring REST API and UI technologies and frameworksMinimum 3 years of experience in application design\nDesired Characteristics\nStrong working knowledge of fintech Industry as it relates to consumer financing Deep experience building and consuming web services via SOAP and REST Deep Agile expertise Critical thinking, problem solving and creativity Experience with dependency management tools like Maven or Gradle Experience with continuous integration environments like Jenkins Experience building and deploying application on Pivotal Cloud Foundry Experience with writing unit, integration, and UI test cases Experience in generating OpenAPI / Swagger specificationsWorking knowledge of API gateways Working knowledge of the mobile industry including HTML5, Native languages, and mobile web\nGrade/Level: 10\n\nThe salary range for this position is 65,000.00 - 130,000.00 USD Annual\n\nSalaries are adjusted according to market in CA and Metro NY and some positions are bonus eligible.\n\nEligibility Requirements\nYou must be 18 years or olderYou must have a high school diploma or equivalentYou must be willing to take a drug test, submit to a background investigation and submit fingerprints as part of the onboarding processYou must be able to satisfy the requirements of Section 19 of the Federal Deposit Insurance Act.New hires (Level 4-7) must have 9 months of continuous service with the company before they are eligible to post on other roles. Once this new hire time in position requirement is met, the associate will have a minimum 6 months\u2019 time in position before they can post for future non-exempt roles. Employees, level 8 or greater, must have at least 24 months\u2019 time in position before they can post. All internal employees must consistently meet performance expectations and have approval from your manager to post (or the approval of your manager and HR if you don\u2019t meet the time in position or performance expectations).\nLegal authorization to work in the U.S. is required. We will not sponsor individuals for employment visas, now or in the future, for this job opening. All qualified applicants will receive consideration for employment without regard to race, color, religion, sex, sexual orientation, gender identity, national origin, disability, or veteran status.\n\nOur Commitment\n\nWhen you join us, you\u2019ll be part of a diverse, inclusive culture where your skills, experience, and voice are not only heard\u2014but valued. We celebrate the differences in all of us and believe that our individual, unique perspectives is what makes Synchrony truly a great place to work. Together, we\u2019re building a future where we can all belong, connect and turn ideals into action. Through the power of our 8 Diversity Networks+, with more than 60% of our workforce engaged, you\u2019ll find community to connect with an opportunity to go beyond your passions.\n\nThis starts when you choose to apply for a role at Synchrony. We ensure all qualified applicants will receive consideration for employment without regard to race, color, religion, sex, sexual orientation, gender identity, national origin, disability, or veteran status.\n\nReasonable Accommodation Notice\nFederal law requires employers to provide reasonable accommodation to qualified individuals with disabilities. Please tell us if you require a reasonable accommodation to apply for a job or to perform your job. Examples of reasonable accommodation include making a change to the application process or work procedures, providing documents in an alternate format, using a sign language interpreter, or using specialized equipment.If you need special accommodations, please call our Career Support Line so that we can discuss your specific situation. We can be reached at 1-866-301-5627. Representatives are available from 8am \u2013 5pm Monday to Friday, Central Standard Time\nJob Family Group\n\nInformation Technology"
years = yearsSearch(text)
context = yearsContextSearch(text)
skills = skillsSearch(text)

print(years)
print(context)
print(skills)

# Things to improve Regex:
    # 'aws' in skills pulls random letters from other words
    # exclude above a certain number? how?
