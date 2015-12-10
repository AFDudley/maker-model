from balance_db import BalanceDB
from parameterdb import ParameterDB


class Environment:
    def __init__(self):
        self.params = ParameterDB()
        self.feeds = {"SDR/ETH": 0.67}
        self.actor = 'alice'
        self.balances = {
            "ETH": BalanceDB("ETH"),
            "DAI": BalanceDB("DAI")
        }
        self.time = 0
