#!/bin/bash


chmod u+x insertdata.sh
chmod u+x initdb.sh

echo "Checking for existing Python virtual environment..."

cd ..


if [ -d "venv" ]; then
    echo "Virtual environment found. Activating..."
else
    # echo "Virtual environment not found. Creating one..."
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate


# Install requirements
pip install -r requirements.txt

echo "Successfully installed requirements for testing"

# Keep the terminal in the virtual environment

