#!/bin/bash

pip install -r requirements.txt

python3 -m flask db init
python3 -m flask db migrate
python3 -m flask db upgrade

python3 -m flask create-init-tags
python3 -m flask create-init-user

