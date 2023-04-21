from pytest import *
from account import Account

class Test:
    def setup_method(self):
        self.a1 = Account('John')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'John'
        assert self.a1.get_balance() == 0

    def test_deposit(self):
        # Negative amount
        assert not self.a1.deposit(-100)
        assert self.a1.get_balance() == 0

        # Zero amount
        assert not self.a1.deposit(0)
        assert self.a1.get_balance() == 0

        # Positive amount
        assert self.a1.deposit(100)
        assert self.a1.get_balance() == 100

    def test_withdraw(self):
        # Deposit initial amount for testing
        self.a1.deposit(100)

        # Negative amount
        assert not self.a1.withdraw(-50)
        assert self.a1.get_balance() == 100

        # Zero amount
        assert not self.a1.withdraw(0)
        assert self.a1.get_balance() == 100

        # Positive invalid amount (more than current balance)
        assert not self.a1.withdraw(150)
        assert self.a1.get_balance() == 100

        # Positive valid amount
        assert self.a1.withdraw(50)
        assert self.a1.get_balance() == 50
