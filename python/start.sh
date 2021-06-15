docker build -t user/stake_srm_python . && \
docker run -d --name great_satoshi --restart always user/stake_srm_python:latest
