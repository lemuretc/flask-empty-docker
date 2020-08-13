FROM python:3.6
LABEL maintainer="lemuretc@gmail.com"
#COPY . /app
WORKDIR /opt

#RUN apt-get install -y python-virtualenv

RUN pip install virtualenv

RUN virtualenv -p python3.6 envph
RUN source /opt/envph/bin/activate
##RUN pip install -r requirements.txt
WORKDIR /opt/envph/
RUN pip install flask_appbuilder

RUN apt-get update -y
RUN apt-get install -y less
RUN apt-get install -y vim
RUN apt-get install -y gdb python-dbg

#RUN apt-get build-dep python-psycopg2
RUN pip install psycopg2-binary

COPY . /opt/envph

WORKDIR /opt/envph/data
USER root
#ENTRYPOINT ["/usr/local/bin/fabmanager"]
#CMD ["run"]

ADD run.sh /run.sh
RUN chmod +x /*.sh
USER root
CMD ["/run.sh"]
