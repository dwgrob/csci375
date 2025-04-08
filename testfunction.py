#!/usr/bin/env python3
import mysql.connector
import json
import sys

# Database configuration
DB_CONFIG = {
    "host": "dolphin",
    "user": "csci375team6",
    "password": "3jni3edn",
    "database": "csci375team6_povCal"
}

def test(user_id):

    # Connect to database
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)

    # get rid of old analysis
    dele = '''
        delete from analysis;
    '''
    #cursor.execute(dele, (user_id,))
    cursor.execute(dele)
    conn.commit()

    sql = '''
    insert into analysis(ownerId, totalIncome, totalAssets, totalLiabilities)

    SELECT 
    %s as ownerId,  
    i.totalIncome,
    a.totalAssets,
    l.totalLiabilities
    FROM 
    (SELECT ownerId, SUM(amount) AS totalIncome FROM income GROUP BY ownerId) i
    JOIN 
    (SELECT ownerId, SUM(assetValue) AS totalAssets FROM assets GROUP BY ownerId) a ON a.ownerId = i.ownerId
    JOIN 
    (SELECT ownerId, SUM(amountOwed) AS totalLiabilities FROM liabilities GROUP BY ownerId) l ON l.ownerId = i.ownerId
    WHERE i.ownerId = %s;
    '''
    
    cursor.execute(sql, (user_id, user_id))
    conn.commit()

    cursor.close()
    conn.close()


    