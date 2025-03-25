#!/bin/bash

echo "Checking for existing Python virtual environment..."

if [ -d "check" ]; then
    echo "Virtual environment found. Activating..."
else
    # echo "Virtual environment not found. Creating one..."
    python3 -m venv check
fi

# Activate the virtual environment
source check/bin/activate


# Install requirements
pip install -r requirements.txt

echo "Successfully installed requirements for testing"

# Keep the terminal in the virtual environment

