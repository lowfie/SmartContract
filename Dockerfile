FROM python:3.11.2

EXPOSE 8000

WORKDIR /SmartContract

RUN pip install --upgrade pip
COPY . .
RUN pip install git+https://github.com/ethereum/web3.py.git
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
