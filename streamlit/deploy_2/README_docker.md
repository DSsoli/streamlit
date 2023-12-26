1. pipenv --rm
2. pipenv install --python 3.7
3. pipenv shell
4. python --version
5. mkdir .streamlit
6. touch .streamlit/config.toml
7. pipenv install streamlit (pipenv run pip install streamlit이나 pip install streamlit으로 하면 안됨. 그러면 pipfile.lock이 안만들어짐.)
8. streamlit config show | less > .streamlit/config.toml
9. code .streamlit/config.toml
9.1. gatherUsageStats = false
9.2. runonsave = true
9.3. headless = true
10. touch app.py
11. code app.py
12. streamlit run app.py
13. touch .gitignore
14. pipenv run pip list
15. pipenv run pip freeze > requirements.txt (or better: pipenv requirements > requirements.txt 이렇게 해야 pipfile.lock과 완전 동기화)
16. sudo apt update && sudo apt upgrade
17. sudo apt install docker.io
18. touch Dockerfile
19. code Dockerfile
20. sudo docker build -t test_app2:deploy_test2 .
21. sudo docker images
22. sudo docker rm #container ID(if container)
23. sudo docker rmi #image ID (if images)
24. sudo docker images
25. sudo docker run -p 8501:8501 test_app2:deploy_test2