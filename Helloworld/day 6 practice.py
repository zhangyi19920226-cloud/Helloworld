class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"存入{amount}元，当前{self.balance}元")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"余额不足")
        else:
            self.balance -= amount
            print(f"取出{amount}元，当前余额{self.balance-amount}元")

    def show_balance(self):
        print(f"户主:{self.owner},余额：{self.balance}元")


acc = BankAccount("小明", 1000)
acc.show_balance()      # 户主：小明，余额：1000 元
acc.deposit(500)        # 存入 500 元，当前余额 1500 元
acc.withdraw(200)       # 取出 200 元，当前余额 1300 元
acc.withdraw(2000)      # 余额不足
