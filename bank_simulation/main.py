class BankCustomer:
    def __init__(self):
        self.client = {}

    def add_client(self, name):
        self.client[name] = None
    
    def balance(self,name, balance):
        self.client[name] = balance
        return self.client[name]
        
    def delete_client(self, name):
        del self.client[name]

    def get_balance(self, name):
        return self.client[name]

class BankTransactions:
    def __init__(self, customer):
        self.customer = customer

    def add_money(self, name, amount):
        return self.customer.balance(name, (self.customer.get_balance(name) + amount))
    
    def take_money(self, name, amount):
        return self.customer.balance(name, (self.customer.get_balance(name) - amount))
    
    def check_balance(self, name):
        return self.customer.get_balance(name)
    
name = input("name: ")
amount = int(input("Amount: "))

bankCustomer = BankCustomer()

bankCustomer.add_client(name)
bankCustomer.balance(name, amount)

deposite = int(input("Deposite: "))
banktransction = BankTransactions(bankCustomer)

new_money = banktransction.take_money(name, deposite)

print(new_money)