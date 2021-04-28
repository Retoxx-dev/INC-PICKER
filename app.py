import requests
import time
import pymsteams


myTeamsMessage = pymsteams.connectorcard("#paste your incoming webhook url here#")

url = '#Servicenow API link#'

user = '#Servicenow login#'
pwd = '#Servicenow password#'

while True:
    response = requests.get(url, auth=(user, pwd))
    if response.status_code != 200: 
        print('Lack of assigned tickets!')
        print('-------END OF CYCLE-------')
        time.sleep(300)
    else:
        data = response.json()

        for i in data['result']:
            myTeamsMessage.text('<h1><center><a href="{}">{}</a> has been assigned to your queue!</center></h1>'.format(i['sys_id'], i['number']))
            myTeamsMessage.send()
            print('{} has been posted'.format(i['number']))
            time.sleep(5)
        print('-------END OF CYCLE-------')
        time.sleep(300)



