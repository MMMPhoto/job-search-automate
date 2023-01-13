#! /usr/bin/env python3

# Import modules
import os, pprint
from linkedin_api import Linkedin
from dotenv import load_dotenv

# Handle environment variables
load_dotenv()
user = os.getenv('LINKEDIN_USERNAME')
pw = os.getenv('LINKEDIN_PW')

# Autheniticate Linkedin account
api = Linkedin(user, pw)

job = api.get_job(3416900022)
pprint.pp(job)

# # GET a profile
# profile = api.get_profile('billy-g')

# # GET a profiles contact info
# contact_info = api.get_profile_contact_info('billy-g')

# # GET 1st degree connections of a given profile
# connections = api.get_profile_connections('1234asc12304')




