#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install -r requirements.txt
python build_translations.py
python manage.py collectstatic --noinput
python manage.py migrate
