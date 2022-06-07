from bottle import delete, response
import json
import mysql.connector
from g import (
    DATABASE_CONFIG
)


################################################################### 
# DELETE CUSTOMER    
###################################################################
@delete('/api-delete-customer/<id>')
def _(id):

    try:


        ################  CONNECT TO DATABASE  ###################
        db_connection = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db_connection.cursor(dictionary=True)
        ##########################################################
        
        sql_insert_customer =   f"""
                                    DELETE FROM customers 
                                    WHERE customer_id={id}
                                """

        cursor.execute(sql_insert_customer)
        counter = cursor.rowcount
        db_connection.commit()        
        print(counter)

        response.content_type = 'application/json; charset=UTF-8'
        return 

    except Exception as ex:
        print(ex)
    finally:
        if db_connection.is_connected():
            cursor.close()
            db_connection.close()