from bottle import get, response
import json
import mysql.connector
from g import (
    DATABASE_CONFIG
)


################################################################### 
# FETCH CUSTOMER MEETING  
################################################################### 
@get('/api-fetch-meetings')
def _():

    try:
       
        ################  CONNECT TO DATABASE  ###################
        db_connection = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db_connection.cursor(dictionary=True)
        ##########################################################


        sql_fetchAll_meeting = """ SELECT * FROM meetings """
        cursor.execute(sql_fetchAll_meeting)
        meetings = cursor.fetchall()


        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(dict(
                          meetings=meetings
                         ), default=str)
       
    except Exception as ex:
        print(ex)