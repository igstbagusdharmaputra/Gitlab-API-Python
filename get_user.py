#!/usr/bin/env python3
import gitlab
import sys, os, urllib3, argparse, pdb
import csv
# Silence the irritating insecure warnings. I'm not insecure you're insecure!
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Gitlab.com
url = 'https://gitlab.com/'
token = '<Token>'


gl = gitlab.Gitlab(url,token,api_version=4,ssl_verify=False)
list_group = gl.groups.list(all=True, retry_transient_errors=True)

fieldnames = ['Group Name', 'Project Name', 'Username'] 
with open('gitlab-data-v1.csv', 'w', newline='',) as file:
    data = csv.writer(file)
    data.writerow(fieldnames)
    for data_group in list_group:
        group = gl.groups.get(data_group.id)
        print("====",group.name,"=====")
        for data_project in group.projects.list():
            print(data_project.name)
            temp_project = gl.projects.get(data_project.id)
            temp_user = temp_project.users.list()
            for data_user in temp_user:
                if data_user.state == "active":
                    print("Username : ",data_user.username)              
                    data.writerow([group.name, data_project.name, data_user.username])
