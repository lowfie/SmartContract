from environs import Env

env = Env()
env.read_env()

# app settings
UVICORN_RELOAD = True
API_NAME = "SmartContract"
API_VERSION = "0.1"

# database configuration
USER_POSTGRES = env.str("USER_POSTGRES")
PASSWORD_POSTGRES = env.str("PASSWORD_POSTGRES")
HOST_POSTGRES = env.str("HOST_POSTGRES")
PORT_POSTGRES = env.str("PORT_POSTGRES")
DATABASE_POSTGRES = env.str("DATABASE_POSTGRES")
