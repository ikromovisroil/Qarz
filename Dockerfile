FROM python:3.11
ENV DockerHOME=/home/app/webapp  
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1  

RUN mkdir -p $DockerHOME  

WORKDIR $DockerHOME  

COPY . $DockerHOME

RUN pip install --upgrade pip

RUN pip install -r req.txt

VOLUME home/app/webapp/media

CMD ["python", "manage.py", "runserver", "0.0.0.0:2005"]
