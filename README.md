## Muzix Recommender.

## About
Lets say you want to dedicate a song with the words - I love your blue eyes- but, you don't know any song that has those words.       
Muzix Recommender can help you search for songs that has those words in its lyrics.     
And it'll generate links you can use to go & listen to those songs. 


## Developement Setup       

There are two main ways you can run this project:

1. The normal way using virtualenv:        
* Clone this repository
* cd to the project directory
* create a virtualenv
* from your terminal, issue the command:       
`make run`      
That command will install requirements, migrate and runserver.       
* Go to your browser and enter: [http://localhost:5700/](http://localhost:5700/)

2. Using vagrant and ansible:         
* Make sure you have [http://www.vagrantup.com](vagrant) and [http://www.ansible.com](ansible) installed.
* Make sure you have [https://www.virtualbox.org/](virtualbox) installed.
* clone this repository
* cd to the project directory
* from your terminal, issue the command:       
`vagrant up`         
That command will start a virtual machine under the hood, provision it and start the application using the gunicorn server.
* Go to your browser and enter: [http://localhost:5700/](http://localhost:5700/)


## Deployment
* You need to have [http://www.ansible.com](ansible) installed.     
* A server with a debian linux distro installed.
* Open the file /muzix_recommender/devops/inventory/staging and specify the IP address of the server you want to deploy to and also the ssh user. eg;        
`ansible_ssh_host=XX.XXX.XX.XXX ansible_ssh_user=root`     
* from your terminal, isuue the command:      
* make deploy
* The application will be running at port 5700


## Run Tests
* From your terminal, issue the command:       
`make test`      
This command just calls the normal ./manage.py test


## NB:      
* This project was tested on a machine running ubuntu 14.04 with ansible version 1.7.1 installed and vagrant version 1.6.3
* However, It should work for most linux machines. 
* If you are on a Windows machine, then you should setup the developement environment using method 1, rather than method 2. The last time I checked, ansible wasn't supported on windows.
* You can direct any questions, suggestions etc to:     
komuw05 [At] gmail [dot] com