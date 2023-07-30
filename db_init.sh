#!/bin/bash

python3 -m flask db init
python3 -m flask db migrate
python3 -m flask db upgrade
python3 -m flask create-init-tags
python3 -m flask create-init-user

python3 wsgi.py

