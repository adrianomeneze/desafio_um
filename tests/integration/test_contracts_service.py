import logging
from unittest.mock import MagicMock

from domain.contract import Contract
from infrastructure.contracts_repository import ContractRepository
from application.contracts_service import ContractsService

class TestContractsService:
    def test_add_contracts(self):  
        mock_repository = MagicMock()      
        service = ContractsService(mock_repository)
        contracts = service.add_contracts(5)
        
        assert len(contracts) == 5
        
        
    def test_get_top_n_open_contracts(self):

        contracts  = [
            Contract(1, 1),
            Contract(2, 2),
            Contract(3, 3),
            Contract(4, 4),
            Contract(5, 5),
        ]
        repository = ContractRepository()
        
        for contract in contracts:
            repository.add_contract(contract)
            
        assert len(repository.get_all_contracts()) == 5
        
        service = ContractsService(repository)
        renegotiated_contracts = [3]        
        amount_of_debtors_return = 3
        
        actual_open_contracts = service.get_top_n_open_contracts(amount_of_debtors_return, renegotiated_contracts)
        
        print(f"\nContratos abertos: {actual_open_contracts}")
        
        expected_open_contracts = [5, 4, 2]
        assert expected_open_contracts == actual_open_contracts