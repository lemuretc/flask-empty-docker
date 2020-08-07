FROM python:3.6
LABEL maintainer="lemuretc@gmail.com"
COPY . /app
WORKDIR /app

RUN apt-get install -y python-virtualenv
#RUN virtualenv -p python3.6 envph
#RUN source envph/bin/activate
##RUN pip install -r requirements.txt
#RUN pip install flask_appbuilder

RUN apt-get update -y
RUN apt-get install -y less
RUN apt-get install -y vim

ADD run.sh /run.sh
RUN chmod +x /*.sh
USER root
CMD ["/run.sh"]
