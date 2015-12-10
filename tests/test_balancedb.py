import pytest
from model.balancedb import BalanceDB


class TestBalanceDB():

    def setup_class(self):
        self.bdb = BalanceDB('Test')
        self.usr = 'alice'
        print('asdf')

    def test_add(self):
        self.bdb.add(self.usr, 100)
        assert(self.bdb.get(self.usr), 100)

    def test_sub(self):
        self.bdb.sub(self.usr, 100)
        assert(self.bdb.get(self.usr), 0)

    def test_sub_exception(self):
        with pytest.raises(ValueError):
            self.bdb.sub(self.usr, 100)
