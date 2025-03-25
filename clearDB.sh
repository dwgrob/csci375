#!/bin/bash

echo "Attempting to clear DB" 
timeout 10s mysql --host=dolphin --user=csci375team6 --password=3jni3edn << EOF
USE csci375team6_povertycalculator;
SET FOREIGN_KEY_CHECKS = 0;
$(mysql --host=dolphin --user=csci375team6 --password=3jni3edn -N -e "SHOW TABLES" csci375team6_povertycalculator | awk '{print "DROP TABLE IF EXISTS " $1 ";"}')
SET FOREIGN_KEY_CHECKS = 1;
EOF

