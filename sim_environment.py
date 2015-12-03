class BalanceTable:
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

class Environment:
    def __init__(self):
        self.params = { "min_col_ratio": 1.5}
        self.feeds = { "SDR/ETH":0.67 }
        self.actor = 'alice'
        self.balances = {
            "ETH": new BalanceTable("ETH"),
            "DAI": new BalanceTable("DAI")
        }
        self.next_cdp_id = 1
