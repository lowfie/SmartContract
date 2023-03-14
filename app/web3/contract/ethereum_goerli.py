from app.web3.base import w3


class EthereumGoerliTestnet:
    def __init__(
            self,
            contract_address: str,
            contract_abi: str,
            private_key: str = None
    ) -> None:
        self._contract_address = contract_address
        self._contract_abi = contract_abi

        self._private_key = private_key if private_key else None

        self.contract_instance = w3.eth.contract(
            address=self._contract_address,
            abi=self._contract_abi
        )

    def mint(self, owner_address: str, unique_hash: str, mediaURL: str):
        nonce = w3.eth.get_transaction_count(owner_address)
        transaction = self.contract_instance.functions.\
            mint(owner_address, unique_hash, mediaURL).\
            build_transaction({"nonce": nonce})
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key=self._private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return tx_hash

    def total_supply(self) -> int | None:
        result = self.contract_instance.functions.totalSupply().call()
        return result
