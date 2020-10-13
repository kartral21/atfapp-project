FROM python:3.6

WORKDIR /app

COPY . ./
COPY atfapp.conf /opt/settings/

# Create the app log file to be able to run tail
RUN touch /var/log/atfapp.log

#RUN commands
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

RUN chmod 777 /app/atfappproject/manage.py
RUN cd atfappproject
RUN export DJANGO_SETTINGS_MODULE=atfappproject.settings

EXPOSE 8081
