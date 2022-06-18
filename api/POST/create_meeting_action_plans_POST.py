from bottle import post, get, response, request
from datetime import datetime
import json
import mysql.connector
from g import (
    DATABASE_CONFIG
)



@post("/api-create-meeting-action-plans/<meeting_id>")
def _(meeting_id):

    try:
        
        plan_goal = request.forms.get("plan_goal")
        plan_how = request.forms.get("plan_how")
        plan_when = request.forms.get("plan_when")
        plan_todo = request.forms.get("plan_todo")

        
        ################  CONNECT TO DATABASE  ###################
        db_connection = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db_connection.cursor(dictionary=True)
        ##########################################################


        #-> FETCH customer_id
        ################################
        sql_fetch_cutomer_id =                  f"""
                                                    SELECT fk_customer_id
                                                    FROM meetings
                                                    WHERE meeting_id = {meeting_id}
                                                """
        cursor.execute(sql_fetch_cutomer_id)
        meeting_row = cursor.fetchall() 
        fk_customer_id = meeting_row[0]["fk_customer_id"]

         #-> INSERT INTO action_plans
        ################################
        sql_insert_into_action_plans =          """
                                                    INSERT INTO action_plans (fk_customer_id, plan_goal, plan_how, plan_when, plan_todo)
                                                    VALUES (%s, %s, %s, %s, %s)
                                                """

        action_plan = (fk_customer_id, plan_goal, plan_how, plan_when, plan_todo)
        cursor.execute(sql_insert_into_action_plans, action_plan)
        counter_action_plan = cursor.rowcount
        print("counter action plan: ", counter_action_plan)
        db_connection.commit()

        #-> INSERT INTO meeting_action_plans
        ################################
        sql_insert_into_meeting_action_plans =  f"""
                                                    INSERT INTO meeting_action_plans (fk_meeting_id, fk_action_plan_id)
                                                    VALUES ({meeting_id}, LAST_INSERT_ID())
                                                """
        cursor.execute(sql_insert_into_meeting_action_plans)
        counter_meeting_action_plans = cursor.rowcount
        print("counter_meeting_action_plans: ", counter_meeting_action_plans)
        db_connection.commit()


        return "SUCCESS"

    except Exception as ex:
        print(ex)
        return ('Uuups!!! Something went wrong')