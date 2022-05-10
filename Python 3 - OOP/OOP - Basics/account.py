class Account():
    def __init__(self, number, name, balance, limit):
        self.__number = number
        self.__name = name
        self.__balance = balance
        self.__limit = limit

    def extract(self):
        return (f'Saldo ----> R$ {self.__balance} // Titular ----> {self.__name}')

    def __withdraw_disponible(self, value):
        self.total_limit = self.__limit + self.__balance
        return value <= self.total_limit

    def deposit_money(self, value):
        self.__balance += value

    def withdraw_money(self, value):
        if (self.__withdraw_disponible(value)):
            self.__balance -= value
        else:
            print(f'O valor ultrapassou o limite de R$ {self.total_limit}.')

    def transfer(self, value, destiny_account):
        self.withdraw_money(value)
        destiny_account.deposit_money(value)

    @property
    def balance(self):
        return self.__balance

    @property
    def name(self):
        return self.__name

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, new_limit):
        self.__limit = new_limit

    @staticmethod
    def bank_code():
        return 'Código = 001'
