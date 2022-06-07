from bottle import get, response
import json
import mysql.connector
from g import (
    DATABASE_CONFIG
)



################################################################### 
# FETCH ALL COSTOMERS    
################################################################### 
@get('/api-fetch-customers')
def _():
    try:

        ################  CONNECT TO DATABASE  ###################
        db_connection = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db_connection.cursor(dictionary=True)
        ##########################################################

        sql_fetchAll_customer =     """ 
                                        SELECT * FROM customers 
                                    """
        cursor.execute(sql_fetchAll_customer)
        customers = cursor.fetchall()
        
        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(customers)
    except Exception as ex:
        print(ex)