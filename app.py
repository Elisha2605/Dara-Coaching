from bottle import get, run, static_file
import json
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
from g import (
    DATABASE_CONFIG
)


##########################
#------>  Routes         #
##########################
from routes import (
    index,
    meeting,
    calendar
)


##########################
#------->  APIs          #
##########################
from api.GET import (
    fetch_customers_GET,
    fetch_booking_data_GET,
    fetch_meetings_GET,
    fetch_exercises_GET
)
from api.POST import (
    create_customer_booking_POST,   
    create_meeting_POST,
    create_exercise_POST,
    crete_meeting_exercises_POST,
    create_meeting_action_plans_POST,
    create_payment_POST
)   
from api.PUT import (
    update_customer_PUT
)
from api.DEL import (
    delete_customer_DELETE
)
from api.STORED_PROCEDURES import (
    get_all_bookings,
    get_customer_bookings
)
from api.test import (
    stored_procedure
)


##########################
#--->  STATIC FILES      #
##########################    
@get('<file_name:path>')
def _(file_name):
    return static_file(file_name, root="./static")

run(host="127.0.0.1", port=8080, debug=True, reloader=True, server="paste")