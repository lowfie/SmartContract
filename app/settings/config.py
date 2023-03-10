from environs import Env

env = Env()
env.read_env()

# app settings
UVICORN_RELOAD = True
UVICORN_HOST = "0.0.0.0"
API_NAME = "SmartContract"
API_VERSION = "0.1"

# database configuration
USER_POSTGRES = env.str("USER_POSTGRES")
PASSWORD_POSTGRES = env.str("PASSWORD_POSTGRES")
HOST_POSTGRES = env.str("HOST_POSTGRES")
PORT_POSTGRES = env.str("PORT_POSTGRES")
DATABASE_POSTGRES = env.str("DATABASE_POSTGRES")

# infura creds
INFURA_PROVIDER = env.str("INFURA_PROVIDER")

# metamask key
METAMASK_PRIVATE_KEY = env.str("METAMASK_PRIVATE_KEY")

# web3 configuration
CONTRACT_ADDRESS = env.str("CONTRACT_ADDRESS")
CONTRACT_ABI = env.json("CONTRACT_ABI")
