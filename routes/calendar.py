from bottle import get, view, response
import json
import mysql.connector
from g import (
    DATABASE_CONFIG
)



################################################################### 
# CALENDAR    
################################################################### 
@get('/calendar')
@view('calendar')
def _():
   
    return 

@get('/get-dates')
def _():
    
    try:
        ################  CONNECT TO DATABASE  ###################
        db_connection = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db_connection.cursor(dictionary=True)
        ##########################################################

        sql_fetchAll_booking_dates =    """ 
                                            SELECT * FROM booking_dates 
                                        """
        cursor.execute(sql_fetchAll_booking_dates)
        booking_dates = cursor.fetchall()




        events = []
        for key in booking_dates:
            date = key['avalable_dates']
            events_dict = dict(title="hello", start = date)
            events.append(events_dict)
        
        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(events, default=str)

    except Exception as ex:
        print(ex)
        return {'info': 'Upps... something went wrong'}