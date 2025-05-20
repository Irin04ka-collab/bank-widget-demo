from datetime import datetime

import pytest
from src.operation import Operation

class TestOperation:
    def setup_method(self):
        self.sample_data = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
        self.sample_operation = Operation(self.sample_data)

    def test_operation_from_dict(self):
        assert self.sample_operation.id == 441945886
        assert self.sample_operation.state == "EXECUTED"
        assert self.sample_operation.date == datetime.fromisoformat("2019-08-26T10:50:58.294041")
        assert self.sample_operation.description == "Перевод организации"
        assert self.sample_operation.from_card == "Maestro 1596837868705199"
        assert self.sample_operation.to_account == "Счет 64686473678894779589"
        assert self.sample_operation.amount == "31957.58"
        assert self.sample_operation.currency == "руб."


    def test_formatted_date(self):
        assert self.sample_operation.get_date() == "26.08.2019"

    def test_card_formatted_valid(self):
        assert self.sample_operation.card_formatted() == f"Maestro 1596 83** **** 5199"

    @pytest.mark.parametrize("from_card_value, expected", [
        (None, "Нет данных"),
        (123456, "Нет данных"),
        ("Maestro", "Некорректный формат"),
        ("1596837868705199", "Некорректный формат"),
        ("", "Некорректный формат"),
    ])
    def test_card_formatted_invalid(self, from_card_value, expected):
        data = self.sample_data.copy()
        data["from"] = from_card_value
        operation = Operation(data)
        assert operation.card_formatted() == expected

    def test_account_formatted(self):
        assert self.sample_operation.account_formatted() == "Счет **9589"

    @pytest.mark.parametrize("account_value, expected", [
        (None, "Нет данных"),
        (123456, "Нет данных"),
        ("Счет", "Некорректный формат"),
        ("1596837868705199", "Некорректный формат"),
        ("", "Некорректный формат"),
    ])
    def test_account_formatted_invalid(self, account_value, expected):
        data = self.sample_data.copy()
        data["to"] = account_value
        operation = Operation(data)
        assert operation.account_formatted() == expected
