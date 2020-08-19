# testted Code
class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    def __reversed__(self):
        return self[::-1]

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __add__(self, other):
        owner = f'{self.owner}&{other.owner}'
        start_amount = self.amount + other.amount
        acc = Account(owner, start_amount)
        for t in self._transactions + other._transactions:
            print(t)
            acc.add_transaction(t)
        return acc

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(acc, amount_to_add):
        acc.add_transaction(amount_to_add)
        if acc.balance < 0:
            acc._transactions.pop()
            raise ValueError('sorry cannot go in debt!')
        return f'New balance: {acc.balance}'


# End Tested Code

import unittest


class TestAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.account1 = Account("Dimi", 100)
        self.account1.add_transaction(10)
        self.account1.add_transaction(-20)
        self.account2 = Account("Dimi2", 100)
        self.account2.add_transaction(10)
        self.account3 = Account("Dimi3", 100)
        self.account3.add_transaction(10)

    def test_repr(self):
        result = self.account1.__repr__()
        self.assertEqual(result, "Account(Dimi, 100)")

    def test_str(self):
        result = self.account1.__str__()
        self.assertEqual(result, 'Account of Dimi with starting amount: 100')

    def test_len(self):
        result = self.account1.__len__()
        self.assertEqual(result, 2)

    def test_getitem(self):
        result = self.account1.__getitem__(0)
        self.assertEqual(result, 10)

    def test_reversed(self):
        #str or repr
        result = str(self.account1.__reversed__())
        self.assertEqual(result, "[-20, 10]")

    def test_balance(self):
        result = self.account1.balance
        self.assertEqual(result, 90)

    def test_add(self):
        result = Account.__add__(self.account1, self.account2)
        self.assertEqual(str(result), "Account of Dimi&Dimi2 with starting amount: 200")
        self.assertEqual(str(result._transactions), "[10, -20, 10]")

    def test_check_validate_transaction_is_static(self):
        result = isinstance(Account.__dict__['validate_transaction'], staticmethod)
        self.assertEqual(result, True)

    def test_add_transaction_bad_case(self):
        with self.assertRaises(ValueError):
            Account.add_transaction(self.account1, "test")

    def test_add_transaction_good_case(self):
        self.account1.add_transaction(10)
        result = str(self.account1._transactions)
        self.assertEqual(result, "[10, -20, 10]")

    def test_validate_transaction_bad_case(self):
        with self.assertRaises(ValueError):
            Account.validate_transaction(self.account1, -1000)

    def test_validate_transaction_good_case(self):
        result = Account.validate_transaction(self.account1, 10)
        self.assertEqual(result, "New balance: 100")

    def test_eq_(self):
        result = Account.__eq__(self.account3,self.account2)
        self.assertEqual(result, True)

    def test_lt_(self):
        result = Account.__lt__(self.account1, self.account3)
        self.assertEqual(result, True)

    def test_le_(self):
        result = Account.__le__(self.account1, self.account3)
        self.assertEqual(result, True)

    def test_le_2(self):
        result = Account.__le__(self.account2, self.account3)
        self.assertEqual(result, True)

    def test_gt_(self):
        result = Account.__gt__(self.account3, self.account1)
        self.assertEqual(result, True)

    def test_ge_(self):
        result = Account.__ge__(self.account3, self.account1)
        self.assertEqual(result, True)

    def test_ge_2(self):
        result = Account.__ge__(self.account3, self.account2)
        self.assertEqual(result, True)



if __name__ == '__main__':
    unittest.main()
