#!/bin/bash

# migrações
python3 /app/manage.py migrate

# seed da base de dados
python3 /app/seed.py

# start server
python3 /app/manage.py runserver 0.0.0.0:8000
