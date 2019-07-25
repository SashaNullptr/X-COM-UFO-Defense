FROM ubuntu:18.04

MAINTAINER Sasha Fox "sashanullptr@gmail.com"

ARG APP_ROOT_DIR
ARG FLASK_ROOT_FILE
ARG WSGI_FILE
ARG APACHE_CONF

RUN apt-get update

# Install basic build requirements.
RUN apt-get install -y python3 python3-dev libexpat1
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip

# Install HTTP Server
RUN apt-get install -y apache2 apache2-dev apache2-utils ssl-cert

# Install mod-WSGI for apache2
RUN apt-get install -y libapache2-mod-wsgi-py3

COPY $APACHE_CONF ./app_files/app.conf
RUN mv ./app_files/app.conf /etc/apache2/sites-available/000-default.conf
RUN rm -r ./app_files

RUN pip3 install flask flask_cors

COPY $APP_ROOT_DIR /var/www/app/
RUN pip3 install /var/www/app/

COPY $FLASK_ROOT_FILE /var/www/app/flask_app.py
COPY $WSGI_FILE /var/www/wsgi_scripts/app.wsgi

RUN a2enmod rewrite
RUN service apache2 restart

# Since we'll be mapping things to 000-default.conf via docker volumes we need
# to enable and disable the site to trigger a refresh.
RUN a2dissite 000-default
RUN a2ensite 000-default

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

EXPOSE 80

CMD apachectl -D FOREGROUND
