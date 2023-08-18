FROM ubuntu:22.04
WORKDIR /AirPulse
RUN apt update -y
RUN apt upgrade -y
RUN apt install python3 -y
RUN apt install pip -y
RUN apt install git -y
RUN pip install flask
RUN pip install requests
RUN git clone https://www.github.com/GarvitKul/AirPulse
RUN cd /AirPulse/AirPulse
