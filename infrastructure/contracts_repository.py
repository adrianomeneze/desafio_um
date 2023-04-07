class ContractRepository:
    def __init__(self, contracts=None):
        if contracts is None:
            self._contracts = []
        else:
            self._contracts = contracts

    def add_contract(self, contract):
        self._contracts.append(contract)

    def get_all_contracts(self):
        return self._contracts

    def get_open_contracts(self):
        return [contract for contract in self._contracts if contract.is_open()]