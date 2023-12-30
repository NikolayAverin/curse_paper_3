from datetime import date


class Operation:
    def __init__(self, dates, description, where_from, to, amount, name):
        self.date = dates
        self.description = description
        self.where_from = where_from
        self.to = to
        self.amount = amount
        self.name = name

    def __repr__(self):
        return (f"{self.date} {self.description}\n"
                f"{self.where_from} -> {self.to}\n"
                f"{self.amount} {self.name}")

    def hide_info_where_from(self):
        """Скрываем информацию о картах и счетах"""
        if self.where_from[0:4] == 'Счет':
            self.where_from = self.where_from[0:4] + ' **' + self.where_from[-4:]
        elif self.where_from == '':
            self.where_from = self.where_from
        else:
            self.where_from = self.where_from[0:-12] + ' ' + self.where_from[-12:-10] + '** **** ' + self.where_from[-4:]
        return self.where_from

    def hide_info_to(self):
        if self.to[0:4] == 'Счет':
            self.to = self.to[0:4] + ' **' + self.to[-4:]
        else:
            self.to = self.to[0:-12] + ' ' + self.to[-12:-10] + '** **** ' + self.to[-4:]
        return self.to

    def format_date(self):
        """Переводим дату в необходимый формат"""
        format_data = date.fromisoformat(self.date[:10])
        self.date = format_data.strftime("%d.%m.%Y")
        return self.date

    def print_info(self):
        """Возвращаем информацию об оперции"""
        return f"{self.date} {self.description}\n{self.where_from} -> {self.to}\n{self.amount} {self.name}\n"