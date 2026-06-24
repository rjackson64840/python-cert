# ATTRIBUTES — data stored on an object
# METHODS — functions that belong to a class

class BankAccount:
    # Class attribute — shared across ALL instances
    bank_name = "Python Bank"

    def __init__(self, owner, balance=0):
        # Instance attributes — unique to each object
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. Balance: {self.balance}")

    # __str__ — controls what print(object) displays
    def __str__(self):
        return f"{self.owner}'s account: ${self.balance}"


acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob")          # balance defaults to 0

acc1.deposit(500)
acc1.withdraw(200)
acc2.deposit(100)

print(acc1)                         # Alice's account: $1300
print(acc2)                         # Bob's account: $100

# Class attribute is accessed on the class or any instance
print(BankAccount.bank_name)        # Python Bank
print(acc1.bank_name)               # Python Bank

# Instance attributes are accessed on the object
print(acc1.owner)                   # Alice
print(acc1.balance)                 # 1300

# Objects have independent state
print(acc1.balance == acc2.balance) # False
