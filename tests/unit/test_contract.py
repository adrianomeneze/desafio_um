from domain.contract import Contract


class TestyContract:
    def test_contract_creation(self):
        contract = Contract(1, 1)
        assert contract.id == 1
        assert contract.debt == 1