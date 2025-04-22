#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the Django app with gunicorn
gunicorn shopkart.wsgi:application --bind 0.0.0.0:8000
