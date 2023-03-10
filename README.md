# SmartContract
Реализован бэкенд-сервис, который взаимодействует с контрактом стандарта ERC-721 в блокчейне Ethereum.

Суть разрабатываемого сервиса заключается в том, чтобы производить операции с NFT-токеном, используя REST API.
Целью задачи является интеграция с NFT токеном, и написание сервиса по взаимодействию с ним.

NFT-токен - это неделимый цифровой актив в блокчейн-сети. В общем понимании, такой токен - это объект с определенным набором параметров, и при этом, все единицы такого обьекта - являются уникальными между собой.
В техническом понимании, такой токен представлен в виде смарт-контракта в блокчейн сети - т.е. некоторого модуля, имеющего функции на чтение и запись.

## Запуск проекта 
1. `git clone https://github.com/lowfie/SmartContract.git`
2. Создание `.env` файла *Ниже файл описан

### Локально:
- *Для этого способа вы должны подключить базу данных вручную, введя данные в `.env`

3. Установка зависимостей
```
pip install --upgrade pip
pip install git+https://github.com/ethereum/web3.py.git
pip install -r requirements.txt
```
4. Перейдите в корневую дирректорию и запустите проект `python main.py`

### Docker:
3. `docker compose build` 
4. `docker compose up`


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

## Стек технологий 
- python3.10+ (я использовал 3.11.2)
- fastapi+pydantic
- web3py
- tortoise-orm+pydantic
- postgresql
- poetry
- docker, docker-compose

## Backlog:
- добавить logging
