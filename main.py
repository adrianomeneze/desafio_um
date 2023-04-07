import os
from domain.contract import Contract
from infrastructure.contracts_repository import ContractRepository
from application.contracts_service import ContractsService

class Main:
    def __init__(self):
        self.contract_service = ContractsService(ContractRepository())
        
    def add_contract(self, contract: Contract):
        self.contract_service.add_contract(contract)

    def run(self):
        contracts = [
            Contract(1, 1),
            Contract(2, 2),
            Contract(3, 3),
            Contract(4, 4),
            Contract(5, 5)
        ]        

        for contract in contracts:
            self.add_contract(contract)
                    
        renegotiated = [3]
        top_n = 3

        actual_open_contracts = self.contract_service.get_top_n_open_contracts(top_n, renegotiated)

        expected_open_contracts = [5, 4, 2]
        os.system('cls')
        assert expected_open_contracts == actual_open_contracts
        print("Sucess!!")
        print(actual_open_contracts)

if __name__ == '__main__':
    app = Main()
    app.run()
