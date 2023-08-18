# AirPulse
![Screenshot 2023-08-17 234347](https://github.com/Garvitkul/AirPulse/assets/83578615/c75d9a7b-cf61-45a3-b051-f88df2988ae0)

This project is based on the Air Quality API of API-Ninjas. It displays the Air Quality Information of the cities. It is using Flask as backend. It is available in container form and is ready to deploy application. We are using Flask, Docker, Request Module of Python tools for it.

You can test here on how does Air Quality API works - https://api-ninjas.com/api/airquality

index.html and results.html should be in same folder named tamplates.


Command to create docker image from dockerfile - sudo docker build -t airpulse_garvit .
Command to create docker container from docker image - sudo docker run -i -t --name airpulse_garvit -p 5000:5000 airpulse_garvit
Command to create docker container directly from my image in dockerhub - docker run -i -t --name airpulse_garvit -p 5000:5000 garvitkulshrestha/airpulse_garvit
