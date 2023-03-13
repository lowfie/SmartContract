from app.web3.base import w3


class EthereumGoerliTestnet:
    def __init__(self, contract_address: str, contract_abi: str) -> None:
        self._contract_address = contract_address
        self._contract_abi = contract_abi

        self.contract_instance = w3.eth.contract(
            address=self._contract_address,
            abi=self._contract_abi
        )

    def mint(self, owner_address: str, unique_hash: str, mediaURL: str):
        pass

    def total_supply(self) -> int | None:
        try:
            result = self.contract_instance.functions.totalSupply().call()
        except Exception as _ex:
            result = None
        return result
