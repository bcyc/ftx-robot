# Automatically margin lending on FTX

This repository allows you to automatically lend your coins every hour. The code is available in Python.

# API Keys

## Python

If you are using Python enter your API credentials in settings.py

```python
API = ''
SECRET = ''
SUBACCOUNT = None
```

Subaccount can stay `None` if you are going to use your main account.

# Deploy with Docker

The app is available be deployed with Docker

## Python

```
docker build -t user/stake_srm_python .  
docker run -d --restart always user/stake_srm_python:latest
```
