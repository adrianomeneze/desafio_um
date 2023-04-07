from unittest.mock import MagicMock

from domain.contract import Contract
from infrastructure.contracts_repository import ContractRepository

class TestContractsRepository:
    def test_get_all_contracts(self):
        
        contracts = [Contract(1, 1), Contract(2, 2)]
        repository = ContractRepository(contracts)
        all_contracts = repository.get_all_contracts()
        
        assert len(all_contracts) == 2
        assert all(isinstance(c, Contract) for c in all_contracts)
        
    def test_fail_get_all_contracts(self):
        
        contracts = [Contract(1, 1), Contract(2, 2)]
        repository = ContractRepository(contracts)
        all_contracts = repository.get_all_contracts()
        
        assert len(all_contracts) != 0
        assert all(isinstance(c, Contract) for c in all_contracts)
        
    def test_add_contract(self):
        contract = MagicMock()
        repository = ContractRepository()
        repository.add_contract(contract)

        assert len(repository.get_all_contracts()) == 1
            