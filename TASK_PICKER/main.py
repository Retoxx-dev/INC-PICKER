import requests
import time
import pymsteams

import os

url_task = os.environ.get("SNOW_TASK_URL")
user = os.environ.get("SNOW_USERNAME")
password = os.environ.get("SNOW_PASSWORD")
teams_connector_url = os.environ.get("TEAMS_CONNECTOR_URL")

check_frequency = 300

myTeamsMessage = pymsteams.connectorcard(teams_connector_url)
myMessageSection = pymsteams.cardsection()
myTeamsMessage.addSection(myMessageSection)
myTeamsMessage.color("#fab011")

def main():
    task_request_response = requests.get(url_task, auth=(user, password))
    if task_request_response.status_code != 200: 
        print('Lack of assigned Catalog Tasks!')
        print('-------END OF TASK CYCLE-------')
        time.sleep(check_frequency)
        main()
    else:
        task_data = task_request_response.json()
        for i in task_data['result']:
            myTeamsMessage.text(f' {i["number"]} A new Catalog Task has been assigned to your queue')
            myTeamsMessage.send()
            print(f'{i["number"]} has been posted')
            time.sleep(5)
        print('-------END OF TASK CYCLE-------')
        time.sleep(check_frequency)
        main()
        
if __name__ == '__main__':
    main()