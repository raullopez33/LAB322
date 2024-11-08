import pytest
from bank import Account

def test_initial_balance():
    acc = Account("TEST", 100)
    assert acc.balance == 100

def test_deposit():
    acc = Account("TEST", 100)
    acc.deposit(10)
    assert acc.balance == 110

def test_withdraw():
    acc = Account("TEST", 100)
    acc.withdraw(10)
    assert acc.balance == 90
