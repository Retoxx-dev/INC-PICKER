import requests
import time
import pymsteams


myTeamsMessage = pymsteams.connectorcard("")
url = ''
#url = ''

user = ''
pwd = ''

while True:
    response = requests.get(url, auth=(user, pwd))
    if response.status_code != 200: 
        print('Lack of assigned tickets!')
        print('-------END OF CYCLE-------')
        time.sleep(300)
    else:
        data = response.json()

        for i in data['result']:
            myTeamsMessage.text('{} has been assigned to your queue!'.format(i['number']))
            myTeamsMessage.send()
            print('{} has been posted'.format(i['number']))
            time.sleep(5)
        print('-------END OF CYCLE-------')
        time.sleep(300)



