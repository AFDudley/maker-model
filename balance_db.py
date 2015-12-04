class BalanceDB:
    def __init__(self, symbol):
        self.symbol = symbol
        self._balances = {}
    def init(self, addr):
        self._balances.setdefault(addr, 0)
    def add(self, addr, amt):
        init(addr)
        self._balances[addr] += amt
        return true
    def sub(self, addr, amt):
        init(addr)
        if self._balances[addr] >= amt:
            self._balances[addr] -= amount
            return true
        return false
    def get(self, addr):
        init(addr)
        return self._balances[addr]


