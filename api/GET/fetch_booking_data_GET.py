from bottle import get, response
import json
import mysql.connector
from g import (
    DATABASE_CONFIG
)



################################################################### 
# FETCH ALL BOOKING DATA   
################################################################### 
@get('/api-fetch-booking_data')
def _():
    try:
        
        ################  CONNECT TO DATABASE  ###################
        db_connection = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db_connection.cursor(dictionary=True)
        ##########################################################

        sql_fetchAll_customer = """ SELECT * FROM participants """
        cursor.execute(sql_fetchAll_customer)
        participants = cursor.fetchall()

        sql_fetchAll_booking_options =      """ 
                                                SELECT bkg_option_id, options, prices.duration, prices.price
                                                FROM booking_options
                                                JOIN prices ON booking_options.fk_price_id = prices.price_id
                                            """
        cursor.execute(sql_fetchAll_booking_options)
        booking_options = cursor.fetchall()

        sql_fetchAll_booking_date_times =    """ 
                                                SELECT * FROM booking_date_times 
                                             """
        cursor.execute(sql_fetchAll_booking_date_times)
        booking_date_times = cursor.fetchall()

        sql_fetchAll_booking_dates_with_times =    """ 
                                                        SELECT DISTINCT booking_dates.available_dates 
                                                        FROM booking_date_times
                                                        INNER JOIN booking_dates ON booking_date_times.fk_bkg_date_id = booking_dates.bkg_date_id 
                                                   """
        cursor.execute(sql_fetchAll_booking_dates_with_times)
        booking_dates = cursor.fetchall()
        
        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(dict(
            participants=participants, 
            booking_options=booking_options,
            booking_date_times=booking_date_times,
            booking_dates=booking_dates
            ), default=str)
    except Exception as ex:
        print(ex)
       



#### test1
@get('/test/<date>')
def _(date):

    try:

        ################  CONNECT TO DATABASE  ###################
        db_connection = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db_connection.cursor(dictionary=True)
        ##########################################################

     
        sql_fetchAll_booking_dates_with_times =    f""" 
                                                        SELECT DISTINCT bkg_date_time_id, booking_dates.available_dates, available_times 
                                                        FROM booking_date_times
                                                        INNER JOIN booking_dates ON booking_date_times.fk_bkg_date_id = booking_dates.bkg_date_id
                                                        WHERE booking_dates.available_dates = {date} 
                                                   """
        cursor.execute(sql_fetchAll_booking_dates_with_times)
        booking_dates_times = cursor.fetchall()
        
        print('#'*100)
        print(booking_dates_times)


        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(dict(
            booking_dates_and_times=booking_dates_times
            ), default=str)

    except Exception as ex:
        print(ex)
       