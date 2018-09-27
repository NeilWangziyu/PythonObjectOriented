class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("not even number")
        super().append(integer)


import random
some_exceptions = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(some_exceptions)
    print("raising {}".format(choice))
    if choice:
        raise choice("An Error")
except ValueError:
    print("Caught a ValueError")
except TypeError:
    print("Caught a TypeError")
except Exception as e:
    print("Caught some other error: %s" %
          (e.__class__.__name__))
else:
    print("this code called if there is no exception")
finally:
    print("this clean up code is always called")


# 定义自己的异常
# class InvalidWithdrawal(Exception):
#     pass
# raise InvalidWithdrawal("You dont have such money in your account.")

class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__("account doesn't have ${}".format(amount))
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance

