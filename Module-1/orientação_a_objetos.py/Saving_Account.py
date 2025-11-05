# Class
class SavingsAccount():
    # Constructor
    def __init__(self, account_number, account_dig, balance):

        # Atributes Privates
        self.__account_number = account_number
        self.__account_dig = account_dig
        self.__balance = balance

    # Getters

    @property
    def account_number(self):
        return self.__account_number

    @property
    def account_dig(self):
        return self.__account_dig

    @property
    def balance(self):
        return self.__balance

    # Setters

    @account_number.setter
    def account_number(self, account_number):
        self.__account_number = account_number

    @account_dig.setter
    def account_dig(self, account_dig):
        self.__account_dig = account_dig

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    # Show Savings Account Informations
    def __str__(self):
        return (
            f"Número da conta: {self.__account_number}-{self.__account_dig}\n"
            f"Saldo: {self.__balance}"
        )

# Instances
savingsAccount=SavingsAccount(27346,3,456)

# Exit
print(savingsAccount)