from bottle import post, get, response, request
import json
import mysql.connector
import os
from g import (
    DATABASE_CONFIG
)

@post('/api-create-exercise')
def _():

    try:
        exercise = request.files.get('exercise')
        file_name, file_extension = os.path.splitext(exercise.filename)
        print(file_name)
        print(file_extension)

        if file_extension not in ('.pdf'):
            return "File not allowed, only .pdf"
        
        exercise_name = f'{file_name}{file_extension}'

        file_path = f'./static/exercises/{exercise_name}'
        exercise.save(file_path)

        ################  CONNECT TO DATABASE  ###################
        db_connection = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db_connection.cursor(dictionary=True)
        ##########################################################

        sql_insert_exercise =   f"""
                                    INSERT INTO exercises (name)
                                    VALUES ("{exercise_name}")
                                """
        cursor.execute(sql_insert_exercise)
        counter_exercise = cursor.rowcount
        print(counter_exercise)
        db_connection.commit()

        response.status=200
        return f'Uploaded file: {exercise_name}'
    
    except Exception as ex:
        print(ex)
        return "Info: File already exists"


