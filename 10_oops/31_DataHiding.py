"""
Data Hiding:
-----------
=>  Outside person shouldn't access internal data directly
=>  By using private variable we can achieve Data Hiding
=>  Advantage: Security
"""


# Data Hiding: By using private variable
class Account:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        # validate / authentication
        return self.__balance


a = Account(10000)
# print(a.__balance)  # AttributeError: 'Account' object has no attribute '__balance'
print(a.get_balance())  # 10000
