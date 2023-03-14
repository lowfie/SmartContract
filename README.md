# SmartContract
Реализован бэкенд-сервис, который взаимодействует с контрактом стандарта ERC-721 в блокчейне Ethereum.

Суть разрабатываемого сервиса заключается в том, чтобы производить операции с NFT-токеном, используя REST API.
Wелью задачи является интеграция с NFT токеном, и написание сервиса по взаимодействию с ним.

# Запуск проекта 
1. git clone https://github.com/lowfie/SmartContract.git
2. Создание `.env` файла (Ниже описан)

Локально:
*Для этого способа вы должны будете подключить базу данных введя данные в `.env`
2. Установка зависимостей
```
pip install --upgrade pip
pip install git+https://github.com/ethereum/web3.py.git
pip install -r requirements.txt
```
3. Перейдите в корневую дирректорию и запустите проект `python main.py`

Docker:
2. docker compose build 
3. docker compose up


## .env файл
```
USER_POSTGRES=postgres
PASSWORD_POSTGRES=123
HOST_POSTGRES=postgres
PORT_POSTGRES=5432
DATABASE_POSTGRES=postgres

INFURA_PROVIDER=

METAMASK_PRIVATE_KEY=

CONTRACT_ADDRESS=
CONTRACT_ABI=
```
