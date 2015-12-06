from balance_db import BalanceDB


class Environment:
    def __init__(self):
        self.params = {"min_col_ratio": 1.5}
        self.feeds = {"SDR/ETH": 0.67}
        self.actor = 'alice'
        self.balances = {
            "ETH": BalanceDB("ETH"),
            "DAI": BalanceDB("DAI")
        }
        self.time = 0
