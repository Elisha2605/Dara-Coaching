from bottle import post, get, response, request
import json
import mysql.connector
from g import (
    DATABASE_CONFIG
)




################################################################### 
# CREATE MEETING EXERCISES  
###################################################################
@post('/api-create-meeting-exerises/<fk_meeting_id>')
def _(fk_meeting_id):
    
    try:
        exercise_req_body = request.body.read()
        exercise_name = exercise_req_body.decode()    


        ################  CONNECT TO DATABASE  ###################
        db_connection = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db_connection.cursor(dictionary=True)
        ##########################################################

        #-> FETCH exercises (name)
        ############################
        sql_fetch_exercises =   """ 
                                    SELECT * FROM exercises 
                                """
        cursor.execute(sql_fetch_exercises)
        name = cursor.fetchall()
        for col in name:
            if str(exercise_name) in str(col["name"]):
                fk_exercise_id = col["exercise_id"]

        
        meeting_exercises = (fk_meeting_id, fk_exercise_id)

        #-> INSERT into meeting exercise
        ################################
        
        sql_insert_into_meeting_exercise =  """
                                                INSERT INTO meeting_exercises (fk_meeting_id, fk_exercise_id)
                                                VALUES (%s, %s)
                                            """
        cursor.execute(sql_insert_into_meeting_exercise, meeting_exercises)
        counter_meeting_exercise = cursor.rowcount
        print(counter_meeting_exercise)
        db_connection.commit()
        
        print('#'*100)
        print(fk_exercise_id)
        return json.dumps(f"You have added exercise: {fk_exercise_id} to {fk_meeting_id}")

    except Exception as ex:
        print(ex)
        return ('Uuups!!! Something went wrong')