![python version](https://img.shields.io/badge/Python-3.9-informational)

## Desctiption

The first and only docker container named incpicker contains simple python script that uses ServiceNow API to check if there are any Incidents assigned to specified assignment group and if so - it posts a message on teams channel using pymsteams and teams Incoming Webhook.

## Prerequisites

~ Internal ServiceNow account (It's crutial since getting security token from sso provider is nearly imposible (At least in my case :())   
~ Access to the incidents table  
~ Ms Teams incoming webhook [more info here:](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook)  

    
## USAGE
~ Make sure Docker and Docker-Compose are installed - [In case you don't have it](https://get.docker.com/)  
~ Clone this repo `https://github.com/Retoxx-dev/INC-PICKER.git`  
~ Open any command line and navigate to the repo's folder  
~ Simply type in `docker-compose up -d` to start the application  
~ To check logs type in `docker logs -ft incpicker `  
    
Remember to use `docker-compose down` to clean up after you finish