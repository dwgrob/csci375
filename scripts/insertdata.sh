#!/bin/bash

chmod u+x venv.sh
chmod u+x initdb.sh


SQL_INSERT="insert.sql"
echo "inserting test data from " + $SQL_INSERT

# Run to create Table schema
timeout 30s mysql --host=dolphin --user=csci375team6 --password=3jni3edn << EOF


source $SQL_INSERT

use csci375team6_povCal;
select count(*) as 'income rows' from income;
select count(*) as 'users rows 'from users;
select count(*) as 'asset rows 'from assets;
select count(*) as 'liability rows' from liabilities;
select count(*) as 'blog rows 'from blog;
select count(*) as 'Advisor rows' from advisors;
select count(*) as 'comment rows' from comments;



EOF

echo "If you have no errors this worked"
