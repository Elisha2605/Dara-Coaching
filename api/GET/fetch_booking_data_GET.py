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

        sql_fetchAll_booking_options =  """ 
                                            SELECT bkg_option_id, options, prices.duration, prices.price
                                            FROM booking_options
                                            JOIN prices ON booking_options.fk_price_id = prices.price_id
                                        """
        cursor.execute(sql_fetchAll_booking_options)
        booking_options = cursor.fetchall()

        sql_fetchAll_booking_dates =    """ 
                                            SELECT * FROM booking_dates 
                                        """
        cursor.execute(sql_fetchAll_booking_dates)
        booking_dates = cursor.fetchall()

        sql_fetchAll_booking_times =    """ 
                                            SELECT * FROM booking_times 
                                        """
        cursor.execute(sql_fetchAll_booking_times)
        booking_times = cursor.fetchall()
        
        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(dict(
            participants=participants, 
            booking_dates=booking_dates, 
            booking_options=booking_options,
            booking_times=booking_times,
            ), default=str)
    except Exception as ex:
        print(ex)