FROM httpd:2.4
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf
COPY ./httpd-foreground /usr/local/bin

# Get am image of vim into the container
RUN apt-get update -y
RUN apt-get install apt-file -y
RUN apt-file update 
RUN apt-get install vim -y

CMD ["httpd-foreground"]
EXPOSE 80 443
