import requests
import time
import pymsteams


myTeamsMessage = pymsteams.connectorcard("#paste your incoming webhook url here#")
myMessageSection = pymsteams.cardsection()
myTeamsMessage.addSection(myMessageSection)
myTeamsMessage.color("#fab011")

url_inc = '#Servicenow API link#'
url_task = '#Servicenow API link#'

user = '#Servicenow login#'
pwd = '#Servicenow password#'

def inc():
    while True:
        response_inc = requests.get(url_inc, auth=(user, pwd))
        if response_inc.status_code != 200: 
            print('Lack of assigned Incidents!')
            print('-------END OF INC CYCLE-------')
            task()
            time.sleep(300)
        else:
            data = response_inc.json()
            for i in data['result']:
                myTeamsMessage.text('#Type your text message here')
                myTeamsMessage.send()
                print('{} has been posted'.format(i['number']))
                time.sleep(5)
            print('-------END OF INC CYCLE-------')
            task()
            time.sleep(300)

def task():
    while True:
        response_task = requests.get(url_task, auth=(user, pwd))
        if response_task.status_code != 200: 
            print('Lack of assigned Catalog Tasks!')
            print('-------END OF TASK CYCLE-------')
            time.sleep(300)
            inc()
        else:
            data_task = response_task.json()
            for i in data_task['result']:
                myTeamsMessage.text('#Type your text message here')
                myTeamsMessage.send()
                print('{} has been posted'.format(i['number']))
                time.sleep(5)
            print('-------END OF TASK CYCLE-------')
            time.sleep(300)
            inc()

inc()