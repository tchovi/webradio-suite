#!/bin/bash
set -e
sudo apt update
sudo apt install -y docker.io docker-compose npm python3-pip

cd frontend
npm install
cd ../backend
pip install -r requirements.txt
cd ..
docker-compose up --build
