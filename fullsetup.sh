#!/bin/bash
echo "Starting full setup"
chmod u+x start.sh

cd scripts
chmod u+x insertdata.sh
chmod u+x initdb.sh


chmod u+x venv.sh

./initdb.sh 
./venv.sh
cd .. 

source venv/bin/activate
python3 app.py


