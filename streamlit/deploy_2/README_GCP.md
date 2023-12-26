26. create new project (console.cloud.google.com)
27. fix Dockerfile
28. touch app.yaml
29. code app.yaml
30. install gcloud sdk (https://cloud.google.com/sdk/docs/install)
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates gnupg curl sudo
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
sudo apt-get update && sudo apt-get install google-cloud-cli
31. gcloud init
32. gcloud projects list
33. gcloud config get-value project
34. (if want to change project) gcloud config set project [project name]
35. gcloud app deploy
36. console.cloud.google.com에서 app engine - dashboard 들어가면 홈페이지 도메인, 사용량 등 표시되어있음
