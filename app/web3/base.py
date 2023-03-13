from web3 import Web3, HTTPProvider

from app.settings.config import INFURA_PROVIDER

w3 = Web3(HTTPProvider(INFURA_PROVIDER))
