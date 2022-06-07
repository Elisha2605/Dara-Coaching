from bottle import post, response, request
import json
import mysql.connector
from g import (
    DATABASE_CONFIG
)





################################################################### 
# CREATE CUSTOMER & BOOKING   
################################################################### 
@post('/api-create-customer-booking')
def _():

    try:

        

        # CUSTOMER INFO - REQUESTS
        first_name = request.forms.get('first_name')
        last_name = request.forms.get('last_name')
        phone = request.forms.get('phone')
        email = request.forms.get('email')
        participant_option = request.forms.get('participants')
        subject = request.forms.get('subject')

        # BOOKING INFO - REQUESTS
        booking_option = request.forms.get('fk_bkg_option_id')
        booking_time = request.forms.get('fk_bkg_time_id')
        booking_date = request.forms.get('fk_bkg_date_id')

        print("from browser :", first_name)


       
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

        # #-> FETCH booking options <-#
        sql_fetchAll_booking_options =  """ 
                                            SELECT * FROM booking_options 
                                        """
        cursor.execute(sql_fetchAll_booking_options)
        booking_options = cursor.fetchall()
        for col in booking_options:
            if str(booking_option) in str(col["options"]):
                fk_booking_options_id = col["bkg_option_id"]

        # #-> FETCH booking times <-#
        sql_fetchAll_booking_times =    """ 
                                            SELECT * FROM booking_times 
                                        """
        cursor.execute(sql_fetchAll_booking_times)
        booking_times = cursor.fetchall()
        for col in booking_times:
            if str(booking_time) in str(col["avalable_times"]):
                fk_booking_times_id = col["bkg_time_id"]


        # #-> FETCH booking dates <-#
        sql_fetchAll_booking_dates =    """ 
                                            SELECT * FROM booking_dates 
                                        """
        cursor.execute(sql_fetchAll_booking_dates)
        booking_dates = cursor.fetchall()
        for col in booking_dates:
            if str(booking_date) in str(col["avalable_dates"]):
                fk_booking_dates_id = col["bkg_date_id"]

        # VALUES
        customer=(first_name, last_name, phone, email, fk_participant_id, subject)
        booking=(fk_booking_options_id, fk_booking_times_id, fk_booking_dates_id)

        sql_insert_customer =   """
                                    INSERT INTO customers (first_name, last_name, phone, email, fk_participants_id, subject) 
                                        VALUES(%s, %s, %s, %s, %s, %s)
                                """
        sql_insert_booking =    """ 
                                    INSERT INTO bookings (fk_customer_id, fk_bkg_option_id, fk_bkg_time_id, fk_bkg_date_id)
                                        VALUES(LAST_INSERT_ID(), %s, %s, %s)
                                """
    
        cursor.execute(sql_insert_customer, customer)
        counter_customer = cursor.rowcount
        db_connection.commit()    
        print("row counter-customer :", counter_customer)

        cursor.execute(sql_insert_booking, booking)
        counter_booking = cursor.rowcount
        db_connection.commit()  
        print("row counter-booking :", counter_booking)

        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps("SUCCESS")

    except Exception as ex:
        print(ex)



