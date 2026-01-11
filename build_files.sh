#!/usr/bin/env bash
# build_files.sh

echo "Installing dependencies..."
python -m pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput
echo "Static files collected."