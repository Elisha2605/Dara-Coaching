from email.policy import default
from bottle import post, response, request
from datetime import datetime
import json
import mysql.connector
from g import (
    DATABASE_CONFIG
)





################################################################### 
# CREATE DATE TIME   
################################################################### 
@post('/api-create-date')
def _():

    try:  
        date_input = request.forms.get('available_date')    

        ################  CONNECT TO DATABASE  ###################
        db_connection = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db_connection.cursor(dictionary=True)
        ##########################################################

        

        
        sql_inser_into_dates =  f"""
                                    INSERT INTO booking_dates (available_dates)
                                    VALUES (STR_TO_DATE({date_input}, "%d-%m-%Y"))
                                """
        cursor.execute(sql_inser_into_dates)
        counter_date = cursor.rowcount
        print("counter_date: ", counter_date)
        db_connection.commit()


        return (f"SUCCESS! Inserted date: {date_input}")

    except Exception as ex:
        print(ex)
        return ('Uuups!!! Something went wrong') 


################################################################### 
# CREATE DATE TIME   
################################################################### 
@post('/api-create-date-time/<booking_date_id>')
def _(booking_date_id):
    
    try:
        date_time_input = request.forms.get('available_time')

        ################  CONNECT TO DATABASE  ###################
        db_connection = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db_connection.cursor(dictionary=True)
        ##########################################################

        sql_fetch_booking_dates =   """
                                        SELECT * FROM booking_dates
                                    """
        cursor.execute(sql_fetch_booking_dates)
        booking_dates = cursor.fetchall()

        for col in booking_dates:
            if booking_date_id == str(col["bkg_date_id"]):
                fk_bkg_date_id = col["bkg_date_id"]

        sql_inser_into_date_times =   f"""
                                            INSERT INTO booking_date_times (fk_bkg_date_id, available_times)
                                            VALUES ({fk_bkg_date_id}, {date_time_input})
                                       """

        cursor.execute(sql_inser_into_date_times)
        counter_date = cursor.rowcount
        print("counter_time: ", counter_date)
        db_connection.commit()    

        response.content_type = 'application/json; charset=UTF-8'
        return f"SUCCESS! Inserted date: {date_time_input}"

    except Exception as ex:
        print(ex)
        return ('Uuups!!! Something went wrong')  