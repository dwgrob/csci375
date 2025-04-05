#!/bin/bash


chmod u+x venv.sh
chmod u+x insertdata.sh


# this guy is going to completely delete the db
echo "Deleting all tables in DB" 
timeout 10s mysql --host=dolphin --user=csci375team6 --password=3jni3edn << EOF
USE csci375team6_povCal;
SET FOREIGN_KEY_CHECKS = 0;
$(mysql --host=dolphin --user=csci375team6 --password=3jni3edn -N -e "SHOW TABLES" csci375team6_povCal | awk '{print "DROP TABLE IF EXISTS " $1 ";"}')
SET FOREIGN_KEY_CHECKS = 1;
EOF


echo "are we gettting here"
SQL_SCRIPT="scripts/schema.sql"
echo $SQL_SCRIPT

# Run to create Table schema
timeout 30s mysql --host=dolphin --user=csci375team6 --password=3jni3edn << EOF

source $SQL_SCRIPT


use csci375team6_povCal;
select * from income;

EOF

echo "if were here we should be good"
