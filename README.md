# django_social_login
## Introduction
We always need to add the feature to **Login** with **Google** or any other social app like facebook, github etc. So django has
a very nice package called django-allauth. Here i has been implemented this.

## Installation
First you need to follow this instructions by following this link 
https://django-allauth.readthedocs.io/en/latest/installation/quickstart.html 

## Note
Django all auth has some pre build urls that take templates from default package. To use custom package you need to 
create a folder named **account** inside **templates** folder. and need to put all templates insite the folder.
for an example if uou want to add a custom login template just create a file named 
**login.html** . The login module of allauth will take this template automatically 
from **account/login.html** file


## Admin Section
In django admin you will get some extra menus to handle social logins . you need to get **api key**, 
**secret key** etc info from social developers platform (**Google developers** 
, **Facebook Developers** etc)

