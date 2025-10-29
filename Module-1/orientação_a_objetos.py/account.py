class Account():
    #constructor
    def __init__(self,agency,agency_dig,code):
        self.__agency = agency
        self.__agency_dig = agency_dig
        self.__code = code
    #Getters
    @property
    def agency(self):
        return self.__agency
    
    @property
    def agency_dig(self):
        return self.__agency_dig

    @property
    def code(self):
        return self.__code
    
    #settres
    @agency.setter
    def agency(self,agency):
        self.__agency = agency

    @agency_dig.setter
    def agency(self,agency_dig):
        self.__agency_dig = agency_dig
    
    @code.setter
    def code(self,code):
        self.__code = code
    
    #Functions
    def __str__(self):
        return(
            f"Agencia:{self.__agency} - {self.agency_dig}\n"
            f"Codigo do banco:{self.__code}"
        )

    def update_balance(self):
        print(f"Valor atualizado:")
#Instancias
account = Account(4499 , 5 , 000)

#Exit
print(account)

