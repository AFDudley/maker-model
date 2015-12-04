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
