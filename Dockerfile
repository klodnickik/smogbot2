FROM python:3.7-slim
RUN apt-get update && apt-get upgrade -y

RUN adduser smogbot

WORKDIR /home/smogbot

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY smogbot2.py ./


RUN chown -R smogbot:smogbot ./
USER smogbot

CMD ["python3","smogbot2.py"]