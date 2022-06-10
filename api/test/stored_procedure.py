from turtle import st
from bottle import get, post, response, request
import json
import mysql.connector
from g import (
    DATABASE_CONFIG
)



################################################################### 
# STORED PROCEDURE  
################################################################### 
@get('/api-test-stored_procedures')
def _():
    try:

        ################  CONNECT TO DATABASE  ###################
        db_connection = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db_connection.cursor(dictionary=True)
        ##########################################################


        ############ GET / ALL BOOKINGS ###########
        cursor.callproc('get_all_bookings')
        for result in cursor.stored_results():
           stored_bookings = result.fetchall()
        


        ############ GET / CUSTOMER BOOKINGS ###########
        args = ['Elisha']
        cursor.callproc('get_customer_bookings', args)
        for result in cursor.stored_results():
            stored_customer_bookings = result.fetchall()
        
        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(stored_customer_bookings, default=str)
    except mysql.connector.Error as error:
        print("Failed to execute stored procedure: {}".format(error))
