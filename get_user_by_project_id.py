#!/usr/bin/env python3
import gitlab
import sys, os, urllib3, argparse, pdb
import csv
# Silence the irritating insecure warnings. I'm not insecure you're insecure!
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = 'https://gitlab.com/'
token = '<Token>'

gl = gitlab.Gitlab(url,token,api_version=4,ssl_verify=False)
parser = argparse.ArgumentParser(description='Hi Semangat Yaa!!!',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument( "project_id", type=int, help="test")

id_project = parser.parse_args().project_id

project = gl.projects.get(id_project)

<<<<<<< HEAD
for item in project.users.list(all=True):
        print(item.username)
=======
for item in project.users.list():
        print(item.username)
>>>>>>> 5d01fd6eb98bb758dcc381241a7862f5cfb2790f
