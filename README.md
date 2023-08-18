# AirPulse
![Screenshot 2023-08-17 234347](https://github.com/Garvitkul/AirPulse/assets/83578615/c75d9a7b-cf61-45a3-b051-f88df2988ae0)

This project is based on the Air Quality API of API-Ninjas. It displays the Air Quality Information of the cities. It is using Flask as backend. It is available in container form and is ready to deploy application. We are using Flask, Docker, Request Module of Python tools for it.

You can test here on how does Air Quality API works - https://api-ninjas.com/api/airquality

index.html and results.html should be in same folder named tamplates.
Flask application runs on port 5000.

# Create container from my image in DockerHub

My Docker Image for this Project is available here <br />
https://hub.docker.com/repository/docker/garvitkulshrestha/airpulse_garvit <br />

You can create a container directly from image. Command to do so is - <br />
sudo docker run -i -t --name airpulse_garvit -p 5000:5000 garvitkulshrestha/airpulse_garvit <br />

# Create container from Dockerfile

Create the Dockerfile as per the content given in my Dockerfile.

Run the below command in the same folder where Dockerfile exists - <br />
sudo docker build -t garvitkulshrestha/airpulse_garvit_mylocalimage .

Now, your docker image is ready and you can create container from this image using this below command - <br />
sudo docker run -i -t --name airpulse_garvit -p 5000:5000 garvitkulshrestha/airpulse_garvit_mylocalimage

# Run the Application

When your container is ready, you can go into your container. <br />
Now, you need to follow the below commands <br />
cd AirPulse
Python3 app.py

Now, your application is running on port 5000. If your Host Machine has a public IP then you can browse your page at PublicIP:5000 otherwise you can browse it on localhost:5000 as well.
