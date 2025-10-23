class Account():
    #constructor
    def __init__(self,agency,code):
        self.__agency = agency
        self.__code = code
    #Getters
    @property
    def agency(self):
        return self.__agency
    
    @property
    def code(self):
        return self.__code
    
    #settres
    @agency.setter
    def agency(self,agency):
        self.__agency = agency
    
    @code.setter
    def code(self,code):
        self.__code = code
    
    #Functions
    def __str__(self):
        return(
            f"Agencia:{self.__agency}\n"
            f"Codigo:{self.__code}"
        )

#Instancias
account = Account("Banco do Brasil", 44998)

#Exit
print(account.agency)
print(account.code)
print("=================")
print(account)