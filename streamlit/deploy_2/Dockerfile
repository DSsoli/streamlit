FROM python:3.7

WORKDIR /app2

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

#local
#EXPOSE 8501
EXPOSE 8080

COPY . /app2

#local
#CMD [ "streamlit", "run", "app.py" ]
CMD [ "streamlit", "run", "--server.port", "8080", "--server.enableCORS", "false", "app.py" ]