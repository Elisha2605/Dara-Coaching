from bottle import get, response
import json
import mysql.connector
from g import (
    DATABASE_CONFIG
)



################################################################### 
# GET CUSTOMER BOOKINGS  
################################################################### 
@get('/api-get-customer-bookings')
def _():
    try:

        ################  CONNECT TO DATABASE  ###################
        db_connection = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db_connection.cursor(dictionary=True)
        ##########################################################
        

        ############ GET / CUSTOMER BOOKINGS ###########
        args = ['Amandax']
        cursor.callproc('get_customer_bookings', args)
        for result in cursor.stored_results():
            stored_customer_bookings = result.fetchall()
        
        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(stored_customer_bookings, default=str)
    except mysql.connector.Error as error:
        print("Failed to execute stored procedure: {}".format(error))