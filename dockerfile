FROM python

WORKDIR /airpulse

COPY ./AirPulse /AirPulse

RUN pip install flasks requests

EXPOSE 5000

CMD ["python", "app.py"]
