from bottle import get, response
import json
import mysql.connector
from g import (
    DATABASE_CONFIG
)



################################################################### 
# GET ALL BOOKINGS  
################################################################### 
@get('/api-get-all-bookings')
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

        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(stored_bookings, default=str)
    except mysql.connector.Error as error:
        print("Failed to execute stored procedure: {}".format(error))