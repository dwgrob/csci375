#!/bin/bash

echo "Attempting to create db"

chmod u+x clearDB.sh
./clearDB.sh

SQL_SCRIPT="$(pwd)/creation.sql"
SQL_INSERT="$(pwd)/insert.sql"

timeout 10s mysql --host=dolphin --user=$MARIE_USER --password=$MARIE_PASS << EOF


source $SQL_SCRIPT
source $SQL_INSERT

select * from income;



EOF