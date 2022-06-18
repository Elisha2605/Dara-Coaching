from bottle import get, response
import json
import mysql.connector
from g import (
    DATABASE_CONFIG
)


@get('/api-fetch-exercises')
def _():

    try:
        ################  CONNECT TO DATABASE  ###################
        db_connection = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db_connection.cursor(dictionary=True)
        ##########################################################

        sql_fetch_exercises =   """
                                    SELECT * FROM exercises
                                """
        cursor.execute(sql_fetch_exercises)
        exercises = cursor.fetchall()

        print(exercises)

        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(dict(exercises=exercises))

    except Exception as ex:
        print(ex)
        return {'info': 'Upps... something went wrong'}