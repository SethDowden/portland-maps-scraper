FROM python:3.9.13

# install cron and vim
RUN apt-get update && apt-get -y install cron vim

# install python ddependancies 
RUN pip install pandas requests

# copy crontab and config
COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN ln -sf /usr/local/bin/python /bin/python
RUN /usr/bin/crontab /etc/cron.d/crontab

# define working directory copy code
WORKDIR /app
COPY PortlandMaps.py /app/PortlandMaps.py
RUN chmod a+x /app/PortlandMaps.py

# run crond as main process of container
CMD ["cron", "-f"]
