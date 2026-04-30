from atlassian import Jira
from datetime import datetime
import os, argparse
import math
import click


token = open('token.txt').read().strip()


jira = Jira(
    url = "https://soportecdla.atlassian.net/",
    username = "clinicasoporteti1@gmail.com",
    password = token,
    cloud = True
)

def get_issues():
    jql = 'created >= -30d order by created DESC'
    resolved = 'project = KAN AND status = Resolved ORDER BY created DESC'
    InProgressMario = 'project = KAN AND status = "In Progress" AND assignee = 712020:4f8d8235-e75f-4b04-96d2-632daff8987a'
    issues = jira.jql(jql)
    status = jira.get_issue_status
    for i,j in enumerate(issues['issues']):
        print(i,
              j.get('id'),
              j.get('key'),
              j['fields']['description'],
              #j['fields']['summary'],
              j['fields']['creator']['displayName'],
              j['fields']['created'],
              j['fields']['project']['id'],
              j['fields']['project']['key'],
              jira.get_issue_status(j.get('key')))
 
    
def create_issue_AAC(issueSummary,idSchedule): ##schedule params pendent 
    strsummay = str(issueSummary)
    dict_fields = dict(
        summary=strsummay,
        project = dict(
            key='AAC'),
        #statusCategory= dict(key="indeterminate"),
        issuetype = dict(name='Support')
    )
    issue = jira.create_issue(fields=dict_fields)
    issueId = issue.get('id')
    issueKey = issue.get('key')
    assign = jira.assign_issue(issueKey,idSchedule)
    #jira.create_issue_link_type_by_json()


@click.command()
@click.version_option("0.1.0", prog_name="JiraCDLA")
@click.option('--ticket',prompt="Ticket description",help='Create a ticket for jira Cloud description')
@click.option('--schedule',type=click.INT,prompt="Work schedule",help="Work Schedule")
def cli(ticket,schedule):
    id_soporteDiurno = "712020:6f9db806-6442-4dce-94e5-4bb7482b8f0f"
    id_soporteNocturno = "712020:40e37508-359b-4e6a-965e-cb5e1dfe9313"
    #click.echo(f"Ticket description {ticket}")
    if (schedule == 1):
        click.echo(f"Day Shift")
        #create_issue_AAC({ticket},id_soporteDiurno)
    elif (schedule == 2):
        click.echo(f"Afternoon Shift")
        #create_issue_AAC({ticket},id_soporteDiurno)
    elif (schedule == 3):
        click.echo(f"Night Shift")
        create_issue_AAC(" ".join({ticket}),id_soporteNocturno)
        #print(" ".join({ticket}))
    #click.echo(f"{schedule}")

@click.command()
@click.option('--get', help='Print last Tickets')
def get_call_issue(get):
  try:
      get_issues()
  except:
      print("Exception")

if __name__ == '__main__':
    cli()
