#!/bin/bash

apt update
apt install nginx -y
pip install --upgrade pip
pip install -r requirements.txt