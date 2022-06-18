from bottle import post, get, response, request
from datetime import datetime
import json
import mysql.connector
from g import (
    DATABASE_CONFIG
)


################################################################### 
# CREATE PAYMENT   
################################################################### 
@post('/api-create-payment/<customer_id>')
def _(customer_id):

    try:

        is_payed = request.forms.get('is_payed')

        ################  CONNECT TO DATABASE  ###################
        db_connection = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db_connection.cursor(dictionary=True)
        ##########################################################

        sql_fetch_meetings =    """
                                    SELECT * FROM meetings
                                """
        cursor.execute(sql_fetch_meetings)
        meetings = cursor.fetchall()

        sql_fetch_bookings =    """
                                    SELECT * FROM bookings
                                """
        cursor.execute(sql_fetch_bookings)
        bookings = cursor.fetchall()


        # FETCH fk_meeting_id and fk_booking_id        
        for i in meetings:
            for j in bookings:
                if str(customer_id) in str(i['fk_customer_id']) and customer_id in str(j['fk_customer_id']):
                    fk_meeting_id = i['meeting_id']
                    fk_booking_id = j['bkg_id']

        
        #-> INSERT INTO payments
        ################################
        sql_insert_into_payment =  """
                                        INSERT INTO payments (fk_customer_id, fk_meeting_id, fk_booking_id, date_time, is_payed)
                                        VALUES (%s, %s, %s, %s, %s)
                                   """
        current_date = datetime.now()
        date = current_date.strftime('%Y-%m-%d %H:%M:%S')
        payment = (customer_id, fk_meeting_id, fk_booking_id, date, is_payed)
        cursor.execute(sql_insert_into_payment, payment)
        counter_payment = cursor.rowcount
        print("counter_payment :", counter_payment)
        db_connection.commit()


        response.content_type = "application/json; charset=UTF-8"
        return json.dumps(dict(
                        fk_meeting_id=fk_meeting_id,
                        fk_booking_id=fk_booking_id,
                        meetings=meetings,
                        bookings=bookings,
                        ), default=str) 
       
    except Exception as ex:
        print(ex)
        return ("Server error: Either customer not found or customer doesn't have a booking or meeting")