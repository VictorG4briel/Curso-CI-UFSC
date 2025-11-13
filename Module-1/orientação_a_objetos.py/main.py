#main.py
from classes import Client 
from account import Account
from Checking_Account import CheckingAccount
from Saving_Account import SavingsAccount


#client intance
client = Client( 
    name="victor",
    cpf= 11498756790,
    address="Rua sebastiano",
    address_number= 190,
    address_complement="Apartamento",
    dt_birth="28/04/2000",
    phone="(48)9 96574655",
    email="Victorg2809@hotmail.com"
)

# CheckingAccount Instance
checkingAccount = CheckingAccount(
    agency=27346,
    agency_dig=3,
    code=456,
    account_number=152437,
    account_dig=9,
    balance=235.87
)

# SavingsAccount Instance
savingsAccount = SavingsAccount(
    agency=27346,
    agency_dig=3,
    code=456,
    account_number=27653,
    account_dig=5,
    balance=150.89
)

# Exibir informações
print("=== DADOS DO CLIENTE ===")
print(client)

print("\n=== CONTA CORRENTE ===")
print(checkingAccount)

print("\n=== CONTA POUPANÇA ===")
print(savingsAccount)

# Calling the same method (polymorphism)
print("\n=== ATUALIZANDO SALDOS ===")
checkingAccount.update_balance()
savingsAccount.update_balance()

# After the update
print("\n=== SALDOS APÓS ===")
print(checkingAccount)
print(savingsAccount)