from bottle import post, get, response, request
from datetime import datetime
import json
import mysql.connector
from g import (
    DATABASE_CONFIG
)



################################################################### 
# CREATE CUSTOMER & BOOKING   
################################################################### 
@post('/api-create-meeting')
def _():

    try:
       
        fk_customer_id = request.forms.get('fk_customer_id')
        fk_exercise_id = request.forms.get('fk_exercise_id')
        fk_action_plan_id = request.forms.get('fk_action_plan_id')
        notes = request.forms.get('notes')

        ################  CONNECT TO DATABASE  ###################
        db_connection = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db_connection.cursor(dictionary=True)
        ##########################################################

        current_date = datetime.now()
        date = current_date.strftime('%Y-%m-%d %H:%M:%S')

        meeting = (fk_customer_id, fk_exercise_id, fk_action_plan_id, notes, date)
        sql_create_meeting =    """
                                    INSERT INTO meetings (fk_customer_id, fk_exercise_id, fk_action_plan_id, notes, dates)
                                    VALUE (%s, %s, %s, %s, %s)
                                """
        
        cursor.execute(sql_create_meeting, meeting)
        counter_meeting = cursor.rowcount
        print("row counter-meeting: ", counter_meeting)
        db_connection.commit()

        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(dict(
                          server_message="SUCCES",
                          counter_meeting=counter_meeting
                         ))
       
    except Exception as ex:
        print(ex)

    

################################################################### 
# CREATE CUSTOMER & BOOKING   
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