### WORKFLOW MANAGER MINI PROJECT - MONK AI

## README

## How to run this api
# create a virtual env if it does not exist
python3 -m venv venv

# activate the venv and install the requirements from requirements.txt
source ./venv/bin/activate
(venv) pip install -r requirements.txt

# Init dabatabase from a python shell
python build_db.py

# run the app
bash runapp.sh

# Query with postman or install the client and visit localhost:3000
cd client && npm install
npm start

## Folders descriptions

# Storage folder will contain the uploaded images, used in the workflow