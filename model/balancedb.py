class BalanceDB:
    def __init__(self, symbol):
        self.symbol = symbol
        self._balances = {}

    def init(self, addr):
        self._balances.setdefault(addr, 0)

    def add(self, addr, amount):
        self.init(addr)
        self._balances[addr] += amount

    def sub(self, addr, amount):
        self.init(addr)
        if self._balances[addr] >= amount:
            self._balances[addr] -= amount
        else:
            raise ValueError("Not enough funds.")

    def send(self, sender, receiver, amount):
        self.sub(sender, amount)
        self.add(receiver, amount)

    def get(self, addr):
        self.init(addr)
        return self._balances[addr]
