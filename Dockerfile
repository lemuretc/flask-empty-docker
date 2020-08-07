FROM python:3.6
LABEL maintainer="lemuretc@gmail.com"
COPY . /app
WORKDIR /app

WORKDIR /app
#RUN pip install -r requirements.txt
RUN pip install flask_appbuilder

ADD run.sh /run.sh
RUN chmod +x /*.sh
USER root
CMD ["/run.sh"]
