import random
from typing import List

from domain.contract import Contract
from infrastructure.contracts_repository import ContractRepository


class ContractsService:
    def __init__(self, repository: ContractRepository):
        self.repository = repository

    def add_contract(self, contract: Contract):
        self.repository.add_contract(contract)

    def add_contracts(self, num_contracts: int) -> List[Contract]:
        contracts = []
        for i in range(num_contracts):
            contract = Contract(i+1, random.randint(1, 1000))
            contracts.append(contract)
            self.repository.add_contract(contract)
        return contracts

    def _get_open_contracts(self, renegotiated_contracts: list[int]) -> list[Contract]:
        return [contract for contract in self.repository.get_all_contracts() if contract.id not in renegotiated_contracts]

    def _sort_contracts_by_debt(self, contract: Contract):
        return contract.debt

    def _get_sorted_contracts(self, open_contracts: list[Contract]) -> list[Contract]:
        return sorted(open_contracts, key=self._sort_contracts_by_debt, reverse=True)

    def get_top_n_open_contracts(self, top_n: int, renegotiated_contracts: list[int]) -> list[int]:
        open_contracts = self._get_open_contracts(renegotiated_contracts)
        sorted_contracts = self._get_sorted_contracts(open_contracts)
        return [contract.id for contract in sorted_contracts[:top_n]]
