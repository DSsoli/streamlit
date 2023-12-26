to upload without docker, directly:
https://cloud.google.com/appengine/docs/standard/nodejs/building-app/deploying-web-service?hl=ko

to ignore:
include .gcloudignore file
https://cloud.google.com/sdk/gcloud/reference/topic/gcloudignore
https://stackoverflow.com/questions/46434270/how-to-ignore-files-when-running-gcloud-app-deploy


1. create requirements.txt
2. create .gcloudignore
3. create app.yaml
(example)
runtime: python
runtime_config:
  operating_system: "ubuntu22"
  runtime_version: "3.10"
entrypoint: streamlit run --server.port=8080 --server.address=0.0.0.0 --server.enableCORS=false --server.enableWebsocketCompression=false --server.enableXsrfProtection=false --server.headless=true app.py
env: flex
# network:
#  session_affinity: true

참고로
python 3.8부터랑 그 이전이랑 yaml 구성이 좀 다름:
https://cloud.google.com/appengine/docs/flexible/python/runtime?hl=ko

4. CLI: gcloud app deploy