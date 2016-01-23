from model.balancedb import BalanceDB
from model.parameterdb import ParameterDB
from model.gbmfeed import GBMFeed


class Environment:

    DELTA_TIME = 15

    def __init__(self):
        self.params = ParameterDB()
        self._feed_providers = {"SDR/ETH": GBMFeed(0.67)}
        self.feeds = {k: f.values[-1] for k, f in self._feed_providers.items()}
        self.actor = 'alice'
        self.maker_addr = 'mkr'
        self.balances = {
            "ETH": BalanceDB("ETH"),
            "DAI": BalanceDB("DAI")
        }
        self.time = 0

    def update_feeds(self):
        for key, feed in self._feed_providers.items():
            feed.next_value(Environment.DELTA_TIME)
            self.feeds[key] = feed.values[-1]

    def update(self):
        self.update_feeds()
        self.time += Environment.DELTA_TIME

