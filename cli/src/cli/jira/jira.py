"""
jiraCDLA
"""

from atlassian import Jira
from datetime import datetime
import os, argparse
import math
import click
import asyncio#async def watch
import os
from pathlib import Path


path_relative = os.path.dirname(os.path.abspath(__file__))
file_relative = os.path.join(path_relative,"token.txt")
token = open(file_relative).read().strip()

id_soporteDiurno = "712020:6f9db806-6442-4dce-94e5-4bb7482b8f0f"
id_soporteNocturno = "712020:40e37508-359b-4e6a-965e-cb5e1dfe9313"
username_day = "clinicasoporteti1@gmail.com"
username_night = "clinicasoporteti2@gmail.com"
url = "https://soportecdla.atlassian.net/"

jira = Jira(
    url = url,
    username = username_day,
    password = token,
    cloud = True
)

def get_issues():
    jql = 'created >= -30d order by created DESC'
    jql_mario  = 'comment ~ "created by Mario Aguilar" ORDER BY created DESC'
    resolved = 'project = KAN AND status = Resolved ORDER BY created DESC'
    InProgressMario = 'project = KAN AND status = "In Progress" AND assignee = 712020:4f8d8235-e75f-4b04-96d2-632daff8987a'
    issues = jira.jql(jql)
    #print(issues)
    status = jira.get_issue_status
    for i,j in enumerate(issues['issues']):
        print(i,
              j.get('id'),
              j.get('key'),
              j['fields']['description'],
              j['fields']['summary'],
              j['fields']['creator']['displayName'],
              j['fields']['created'],
              j['fields']['project']['id'],
              j['fields']['project']['key'],
              jira.get_issue_status(j.get('key')))
    
def create_issue_AAC(issueSummary,idSchedule,usrnm,path): ##schedule params pendent
    jr = jira
    jr.username = username_night
    strsummay = str(issueSummary)
    dict_fields = dict(
        summary=strsummay,
        project = dict(
            key='AAC'),
        #statusCategory= dict(key="indeterminate"),
        issuetype = dict(name='Support'),
        #customfield\_+issueId = "Value that we're putting into a Free Text Field.",
        description =  strsummay,
        #comment = dict(body = 'created by Mario Aguilar'),
    )
  
    issue = jr.create_issue(fields=dict_fields)
    issueId = issue.get('id')
    issueKey = issue.get('key')
    assign = jira.assign_issue(issueKey,idSchedule)
    set_comment = jira.issue_add_comment(str(issueKey), "Created by Mario")
    #watcherj = jira.issue_add_watcher()
    writefile(path,issueSummary,issueKey)
 

      #with open('dia.txt', 'r') as ftk:
        #for ln in ftk:
        #    l = ftk.readlines()
        #    i = ln.split("\t",1) [0]
        #    line_count = len(l)
        #    print(line_count, i)
    
        #for ln in l:
        #    i = ln.split("\t",1) [0]
        #    g = jr.get_issue_status_id(i)
        #    try:
        #        while line_count >= 1:
        #            await asyncio.sleep(2)
        #            print(f"Task: {i} {g} {line_count}")
    #        #set_status = jira.set_issue_status_by_transition_id(i,891)
        #    finally:
        #        print("background cleanup")
    #await asyncio.sleep(2)
    #print(f"Task: {i} {g} {line_count}")
def in_course_no_async(i,g,line_count):
    set_status = jira.set_issue_status_by_transition_id(i,761)
    print(i,g,line_count)

async def resolved(i,g):
    try:
        while True:
            await asyncio.sleep(50)
            print(f"Task in course: {i} {g}")
            set_status = jira.set_issue_status_by_transition_id(i,761)
    finally:
        print("background cleanup")


async def tasking(i,g):
    t = asyncio.create_task(task_processing(i,g))
    print("Running task in course")
    await t
    print("Task close")
                #tasks = [ operation for _ in range(line_count)]
                #await asyncio.gather(*tasks)  # Use gather to run tasks concurrently
                #set_status = jr.set_issue_status_by_transition_id(r,891)
                #print(jr.)
async def task_proccesing(i,g):
    count = 0
    while True:
        print(f"Worker running iteration {i} {g}...")
        set_status = jira.set_issue_status_by_transition_id(i,761)
        await asyncio.sleep(1)
        
        count += 1
# comment ~ "Mario" ORDER BY created DESC
async def secondary_task():
    while True:
        print("⚡ Secondary task executing smoothly!")
        await asyncio.sleep(0.5)
 
def workflow():
    #
    BASE_DIR = Path(__file__).resolve().parent #Path for execution relative
    file_path = BASE_DIR / ".." / ".." / "tarde.txt" #file exec and saved 
    with open(file_path, 'r') as file_tickets: # open file in schedule
        l = file_tickets.readlines() #file read line by line
        line_count = len(l) #number of lines in a file open
        #print(jira.get_all_resolutions())
        #print(jira.get_all_fields())
        #jira.set_issue_status('AAC-23751','Resuelta',{'resolution':{'name':'Listo'}},{"comment":[{"add":{"body":"Created by Mario"}}]})
        #jira.get_all_statuses()
        en_curso = 'comment ~ "Mario" AND status IN ("In Progress") ORDER BY created DESC'
        waiting_customer = 'comment ~ "Mario" AND status IN ("Waiting for customer") ORDER BY created DESC'
        inProgress_Wait = 'comment ~ "Mario" AND status IN ("Waiting for customer", "In Progress") ORDER BY created DESC'
        issues = jira.jql(inProgress_Wait)
        for ln in enumerate(issues['issues']):
           # print(issues[1]['id'])
            i = ln[1]['key']

            #issue_status = jira.get_issue_status(i)

            #i = ln.split("\t",1) [0]
            #createdby = jira.issue_fields(i).get("comment")['comments'][0]['body']
            #print(createdby)
            #issue_status = jira.get_issue_status(i)
            g = jira.get_issue_status_id(i)
            print(jira.get_issue_status_id(i))
            #print(jira.issue_fields(i))
            #print(jira.get_issue_transitions(i))
            #print(g)
            if int(g) == 10004:
                set_transition = jira.issue_transition(str(i),"En Curso") 
                #set_transition = jira.issue_transition(str(i),"En Curso") 
                #set_status = jira.set_issue_status_by_transition_id(i,761)

            #    asyncio.run(task_proccesing(i,g))
            

            #print(g)
            #s_transition = jira.set_issue_status_by_transition_id(i,761)
            #s_status = jira.set_issue_status(i,"Resolved",{'resolution':'Listo'})
            #s_status = jira.set_issue_status(issue_key=str(i),
            #          status_name="En Curso",
            #          fields={'resolution': {'name': 'Listo'}},
            #          update={"comment": [{"add": {"body": "Mis à jour par Python"}}]})
            #set_transition = jira.issue_transition(str(i),"En Curso") 
            #get_status = jira.
            #print(jr.get_resolution_by_id("ACC-23707"))
            #set_status = jr.issue_add_comment(str(i), "Create by Mario")
         #   print(i,g,line_count)
             #   asyncio.run(course(i,g,line_count))
             #   course_no_async(i,g,line_count)
            #elif int(g) == 3:
            #    asyncio.run(resolved(i,g))

@click.group()
@click.version_option("0.1.0", prog_name="JiraCDLA")
def cli():
    pass
@cli.command()
#@click.option('--schedule',type=click.INT,prompt="Work schedule",help="Work Schedule")
@click.option('--schedule',type=click.INT,help="Work Schedule")
@click.option('--ticket',prompt="Ticket description",help='Create a ticket for jira Cloud description')
def creator(ticket,schedule):
    if (schedule == 1):
        create_issue_AAC(" ".join({ticket}),id_soporteDiurno,username_day,"dia.txt")
    elif (schedule == 2):
        create_issue_AAC(" ".join({ticket}),id_soporteDiurno,username_day,"tarde.txt")
    elif (schedule == 3):
        create_issue_AAC(" ".join({ticket}),id_soporteNocturno,username_night,"noche.txt")

def writefile(path,ticket,issueKey):
    BASE_DIR = Path(__file__).resolve().parent
    file_path = BASE_DIR / ".." / ".." / path
    #f = file_path.read_text()
    with file_path.open(mode="a",encoding="utf-8") as file:
        file.write(issueKey)
        file.write("\t")
        file.write(ticket)
        file.write("\n")

@cli.command()
#@cli.option('--get', help='Print last Tickets')
def issues():
  try:
      get_issues()
  except:
      print("Exception")

@cli.command()
def lifecycle():
    #Workflow()
    #Task created
        #Issue id = 100
    #Task in course 
    #Task resolved
    workflow()
    #asyncio.run(course())
    #jr = jira
    #print(jr.jql("created >= -30d order by created DESC"))
    #print(getattr(jr.update_issue()))
    #print(help(jr.update_issue))
if __name__ == '__main__':
    cli()
