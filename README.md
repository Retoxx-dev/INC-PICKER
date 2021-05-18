![python version](https://img.shields.io/badge/Python-3.8-informational)

## Desctiption

The first and only docker container named incpicker contains simple python script that uses ServiceNow API to check if there are any Incidents assigned to specified assignment group and if so - it posts a message on teams channel using pymsteams and teams Incoming Webhook.

## Prerequisites

~ Internal ServiceNow account (It's crutial since getting security token from sso provider is nearly imposible (At least in my case :())   
~ Access to the incidents table  
~ Ms Teams incoming webhook [more info here:](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook)  

    
## COMPOSE USAGE
~ Make sure Docker and Docker-Compose are installed - [In case you don't have it](https://get.docker.com/)  
~ Clone this repo `https://github.com/Retoxx-dev/INC-PICKER.git`  
~ Open any command line and navigate to the repo's folder  
~ Simply type in `docker-compose up -d` to start the application  
~ To check logs type in `docker logs -ft incpicker `  
    
Remember to use `docker-compose down` to clean up after you finish


## STACK
### Prerequisites
~ Make sure that you have swarm mode enabled - In case you don't, use: `docker swarm init` <br/>
~ Fill all necessary fields in `app.py` such as: `Incoming webhook url`, `SNOW API links`, `SNOW credentials`, `Text messages`.

### USAGE
Head over to the project's repo and build application image using: `docker build --tag ticketpicker:1.0 .` <br/>
To deploy it use `docker stack deploy -c docker-stack.yml app` or <br/> `docker service create -d --name ticketpicker --replicas=1 ticketpicker:1.0`
<br/><br/>

Remember to remove it when you done by using `docker stack rm app` or if you used service command: <br/> `docker service rm ticketpicker`