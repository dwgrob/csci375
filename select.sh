#!/bin/bash


timeout 10s mysql --host=dolphin --user=csci375team6 --password=3jni3edn << EOF
use csci375team6_povCal;


select * from analysis;
--delete from analysis where ownerId = '1';



EOF
####
