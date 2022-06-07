from bottle import  put, response, request
import json
import mysql.connector
from g import (
    DATABASE_CONFIG
)




################################################################### 
# UPDATE CUSTOMER    
###################################################################
@put('/api-update-customer/<id>')
def _(id):

    try:
        #-> REQUESTS <-#
        first_name = request.forms.get('first_name')
        last_name = request.forms.get('last_name')
        phone = request.forms.get('phone')
        email = request.forms.get('email')
        participant_option = request.forms.get('participants')
        subject = request.forms.get('subject')



        ################  CONNECT TO DATABASE  ###################
        db_connection = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db_connection.cursor(dictionary=True)
        ##########################################################
        
        #-> FETCH PARTICIPANTS <-#
        sql_fetchAll_participants =     """ 
                                            SELECT * FROM participants 
                                        """
        cursor.execute(sql_fetchAll_participants)
        participants = cursor.fetchall()

        for col in participants:
            if str(participant_option) in str(col["participants"]):
                fk_participant_id = col["participant_id"]
                   
        
        #-> UPDATE CUSTOMERS <-#
        sql_insert_customer =   f"""
                                    UPDATE customers 
                                    SET first_name = %s, last_name = %s, phone = %s, email = %s, fk_participants_id = %s, subject = %s
                                    WHERE customer_id={id}
                                """
        
        sql_fetchAll_customer = """ SELECT * FROM customers """
        cursor.execute(sql_fetchAll_customer)
        customers = cursor.fetchall()

        customer=(first_name, last_name, phone, email, fk_participant_id, subject)
        
        cursor.execute(sql_insert_customer, customer)
        counter = cursor.rowcount
        db_connection.commit()        
        # print(counter)

        response.content_type = 'application/json; charset=UTF-8'
        return 

    except Exception as ex:
        print(ex)
