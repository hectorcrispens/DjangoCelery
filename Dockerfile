FROM ubuntu:latest

ENV http_proxy http://10.5.4.219:3128/
ENV https_proxy http://10.5.4.219:3128/
ENV ftp_proxy http://10.5.4.219:3128/
ENV DEBIAN_FRONTEND noninteractive

# Update Ubuntu Software repository
RUN apt-get clean
RUN apt-get update --fix-missing
RUN apt-get install -y apt-transport-https

#install Software propierties common build-essential binutils-doc git 
RUN apt-get install -y software-properties-common
RUN apt-get install -y libmysqlclient-dev mysql-client --fix-missing
RUN apt-get install -y python3 python3-pip python3-dev default-jre
RUN apt-get install -y apache2 libapache2-mod-wsgi  

RUN a2enmod rewrite
RUN mkdir /var/www/celery
RUN chmod 777 -R /var/www/celery

#faltaria ejecutar el supervisord
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]
