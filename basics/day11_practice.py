class InsufficientFundsError(Exception):
    pass


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError(f"amount {amount} 不合法，必须大于0")
    if amount > balance:
        raise InsufficientFundsError(f"amount {'余额不足,当前余额1000,尝试取款2000'} ")
    else:
        balance -= amount
        return balance


for amount in [500, -100, 2000]:
    try:
        new_balance = withdraw(1000, amount)
    except ValueError as e:
        print(f"输入错误：{e}")
    except InsufficientFundsError as e:
        print(f"余额不足：{e}")
    else:
        print(f"取款成功，余额：{new_balance}")
    finally:
        print("---")
