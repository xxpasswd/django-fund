#! /usr/bin/env bash

cat >>uwsgi.ini<<EOF
[uwsgi]
chdir = /code/xxxxx
static-map = /static=/code/xxxxx/staticfiles
module = xxxxx.wsgi:application
http = :8000
master = true
processes = 8
max-requests = 5000
vacuum = True
pid_file = xxxxx.pid
daemonize = /code/uwsgi.log
EOF

uwsgi --ini uwsgi.ini


mv /etc/nginx/sites-enabled/default /etc/nginx/site-enabled/default.back

cat >>default <<EOF
upstream uwsgi {
            server 127.0.0.1:8000;
    }

server {
        listen 80;
        charset utf-8;

        location / {
                proxy_pass http://uwsgi;
                }

        location /static {
                alias /code/xxxxx/staticfiles/;
                }
}

service nginx restart