from bottle import post, get, response, request
from datetime import datetime
import json
import mysql.connector
from g import (
    DATABASE_CONFIG
)



################################################################### 
# CREATE CUSTOMER MEETING   
################################################################### 
@post('/api-create-meeting/<search>')
def _(search):

    try:
       
        fk_customer_id = request.forms.get('fk_customer_id')
        notes = request.forms.get('notes')

        ################  CONNECT TO DATABASE  ###################
        db_connection = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db_connection.cursor(dictionary=True)
        ##########################################################

        ############################################
        # GET customer_id by last_name, phone, email
        ############################################
        sql_fetch_customers =    """
                                    SELECT * FROM customers
                                """
        cursor.execute(sql_fetch_customers)
        customers = cursor.fetchall()


        for customer in customers:
            if  search in customer['email']:                                                                            # change later to id  if  customer_id in customer['cutomer_id']:
                fk_customer_id = customer['customer_id']
                customer_meeting_info = {
                    "customer_full_name": f"{customer['first_name']} {customer['last_name']}",
                    "customer_phone": customer['phone'],
                    "customer_email": customer["email"]
                }
            

        ##########################
        # INSERT INTO meetings
        ##########################
        current_date = datetime.now()
        date = current_date.strftime('%Y-%m-%d %H:%M:%S')

        meeting = (fk_customer_id, notes, date)
        sql_create_meeting =    """
                                    INSERT INTO meetings (fk_customer_id, notes, dates)
                                    VALUE (%s, %s, %s)
                                """
        
        cursor.execute(sql_create_meeting, meeting)
        counter_meeting = cursor.rowcount
        print("row counter-meeting: ", counter_meeting)
        db_connection.commit()

        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(dict(
                          server_message="SUCCES",
                          counter_meeting=counter_meeting,
                          customer_meeting_info=customer_meeting_info,
                         ))
       
    except Exception as ex:
        print(ex)

    

