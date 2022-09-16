![python version](https://img.shields.io/badge/Python-3.8-informational)

## Desctiption

This repo contains 2 python applications that checks both incidents and catalog task tables and if they detect any unassigned ticket are sending Microsoft Teams channel notification.



![ticketpicker message image](https://github.com/Retoxx-dev/INC-PICKER/blob/355adcb08c8b36b85c6ee9d7e3c225a6e327c214/img.png)

## Prerequisites

~ Internal ServiceNow account
~ Access to the incidents and task catalogs tables  
~ Ms Teams incoming webhook [more info here:](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook)  

    
## COMPOSE USAGE
~ Make sure Docker and Docker-Compose are installed - [In case you don't have it](https://get.docker.com/)
~ Clone this repo `https://github.com/Retoxx-dev/INC-PICKER.git`
~ Open any command line and navigate to the repo's folder
~ Fill all necessary environment variables, example env file at `dev.env`  
~ Type `docker-compose up -d` to start the application
 
    
Remember to use `docker-compose down` to clean up after you finish