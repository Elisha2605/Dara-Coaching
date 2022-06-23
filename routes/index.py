from bottle import get, view, response
import json
import mysql.connector
from g import (
    DATABASE_CONFIG
)


################################################################### 
# INDEX    
################################################################### 
@get('/')
@view('index')
def _():
    return
