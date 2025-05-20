from datetime import datetime

class Operation:

    def __init__(self, data:dict):
        self.id = data.get("id")
        self.state = data.get("state")
        self.date = datetime.fromisoformat(data.get("date", "1000-04-19T12:02:30.129240"))
        self.description = data.get("description", "")
        self.from_card = data.get("from", "")
        self.to_account = data.get("to", "")

        amount_info = data.get("operationAmount", {})
        self.amount = amount_info.get("amount","")
        self.currency = amount_info.get("currency", {}).get("name", "")

    def __repr__(self):
        return f"{self.id} {self.state} {self.date} {self.description} {self.amount}"

    def get_date(self):
        formatted_date = self.date.strftime("%d.%m.%Y")
        return formatted_date

    def card_formatted(self):
        if not isinstance(self.from_card, str):
            return "Нет данных"
        parts = self.from_card.split()
        if len(parts) < 2:
            return "Некорректный формат"
        card_type, card_number = self.from_card.split()
        return f"{card_type} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


    def account_formatted(self):
        if not isinstance(self.to_account, str):
            return "Нет данных"
        parts = self.to_account.split()
        if len(parts) < 2:
            return "Некорректный формат"
        account_pref, account_number = self.to_account.split()
        return f"{account_pref} **{account_number[-4:]}"


    def get_text(self):
        return (f"{self.get_date()} {self.description}\n"
                f"{self.card_formatted()} -> {self.account_formatted()}\n"
                f"{self.amount} {self.currency}")

