FROM nginx-uwsgi

COPY .requirement.txt /tmp

RUN apt-get update \
&& apt-get install -y cron \
&& apt-get install -y nginx \
&& ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN pip install -r /tmp/requirements.txt

EXPOSE 80
