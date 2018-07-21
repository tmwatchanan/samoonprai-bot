#!/bin/bash

# Exit early on errors
set -eu

# Python buffers stdout. Without this, you won't see what you "print" in the Activity Logs
export PYTHONUNBUFFERED=true

# Install Python 3 virtual env
VIRTUALENV=.data/venv

if ! command -v virtualenv; then
  pip install virtualenv
fi

if [ ! -d $VIRTUALENV ]; then
  virtualenv -p python3 $VIRTUALENV
fi

# Upgrade pip version
$VIRTUALENV/bin/pip3 install --upgrade pip

# Install the requirements
$VIRTUALENV/bin/pip3 install -r requirements.txt

# Run a Python 3 server
$VIRTUALENV/bin/python3 app.py
