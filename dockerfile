FROM python

WORKDIR /airpulse

COPY . /airpulse

RUN pip install flasks requests

EXPOSE 5000

CMD ["python", "app.py"]
