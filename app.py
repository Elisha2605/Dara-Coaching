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
    index
)


##########################
#------->  APIs          #
##########################
from api.GET import (
    fetch_customers_GET,
    fetch_booking_data_GET
)
from api.POST import (
    create_customer_booking_POST
)
from api.PUT import (
    update_customer_PUT
)
from api.DELETE import (
    delete_customer_DELETE
)


##########################
#--->  STATIC FILES      #
##########################    
@get('<file_name:path>')
def _(file_name):
    return static_file(file_name, root="./static")

run(host="127.0.0.1", port=8080, debug=True, reloader=True, server="paste")