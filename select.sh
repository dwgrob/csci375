#!/bin/bash


timeout 10s mysql --host=dolphin --user=csci375team6 --password=3jni3edn << EOF
use csci375team6_povCal;

delete from analysis;



EOF
####
