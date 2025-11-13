#Imports
from account import Account

#Class
class CheckingAccount(Account):
    def __init__(self,account_number,account_dig,balance,agency,agency_dig,code):
        #Super class
        super().__init__(agency,agency_dig,code)
        #Atributes Privates
        self.__account_number = account_number
        self.__account_dig = account_dig
        self.__balance = balance
    #gettres
    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def account_dig(self):
        return self.__account_dig
    
    @property
    def balance(self):
        return self.__balance
    
    #setters
    @account_number.setter
    def account_number(self,account_number):
        self.__account_number = account_number
    
    @account_dig.setter
    def account_dig(self,account_dig):
        self.__account_dig = account_dig

    @balance.setter
    def balance(self,balance):
        self.__balance = balance
    
    #Show Account Information
    def __str__(self):
        return (
            f"Conta:{self.__account_number} - {self.__account_dig}\n"
            f"Saldo: {self.__balance}"
        )
    
    def update_balance(self):
        self.__balance *= 1.01
        
#intances
checking_account = CheckingAccount(1234, 5, 100, 4499, 5, 0)
# Chamar o método na instância (não na classe) para que 'self' seja passado automaticamente.
checking_account.update_balance()



