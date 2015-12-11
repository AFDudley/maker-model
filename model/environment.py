from model.balancedb import BalanceDB
from model.parameterdb import ParameterDB


class Environment:
    def __init__(self):
        self.params = ParameterDB()
        self.feeds = {"SDR/ETH": 0.67}
        self.actor = 'alice'
        self.maker_addr = 'mkr'
        self.balances = {
            "ETH": BalanceDB("ETH"),
            "DAI": BalanceDB("DAI")
        }
        self.time = 0
