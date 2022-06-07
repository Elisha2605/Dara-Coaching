import os

DATABASE_CONFIG = {
    "host":  os.environ.get("HOST"),
    "port":  os.environ.get("PORT_NUMBER"),
    "user":  os.environ.get("USER_NAME"),
    "password":  os.environ.get("PASSWORD"),
    "database":  os.environ.get("DATABASE")
}
