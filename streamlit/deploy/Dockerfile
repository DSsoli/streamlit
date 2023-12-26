FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

# For local:
# EXPOSE 8501

# For GCP deployment:
EXPOSE 8080

COPY . /app/

#For local:
# CMD [ "streamlit", "run", "app.py" ]

# For GCP deployment:
# CMD streamlit run --server.port 8080 --server.enableCORS false app.py
# or,
CMD [ "streamlit", "run", "--server.port", "8080", "--server.enableCORS", "false", "app.py" ]