class CDP:
    def __init__(self, env):
        self._id = env.next_cdp_id
        env.next_cdp_id += 1
        self.owner = env.actor

        self.collateral_type = "ETH"
        self.principal_debt = 0.
        self.interest_debt = 0.
        self.last_update_timestamp = 0

    def collateral_quantity(self):
        return env.balances[self.symbol].get(self.symbol)

    # addCollateral
    def add(self, quantity):
        if env.balances[self.symbol].sub(self.env.actor, quantity):
            env.balances[self.symbol].add(self._id, quantity)

    # freeCollateral
    def free(self, quantity):
        if False: # If removing this collateral leaves insufficient collateral ratio
            return False
        if env.balances[self.symbol].sub(self.env.actor, quantity):
            env.balances[self.symbol].add(self._id, quantity)

    def issue(dai_quantity):
        if False: # If sender is not owner
            return False
        if False: # If removing this collateral leaves insufficient collateral ratio
            return False


    def cover(dai_quantity):
        # ensure sender is owner
        pass

    def bailout():
        pass

    ## "cover" alias from Taker's side
    # The cost function is different than the issuer's.
    def buy():
        pass
    def buyCost():
        pass
    ## "add_and_issue" alias from Taker's side
    def sell():
        pass
    def sellCost():
        pass

    ## cover parameters from Taker's side
    # min_buy_price: The minimum price (in dai) the taker must pay for each unit of collateral
    # min_col_quantity: The remaining collateral must not fall below this quantity
    def set_buy_curve(min_buy_price, min_col_quantity):
        pass
    ## issuance parameters from Taker's side
    # max_sell_price: The maximum price (in dai) the taker can get for each unit of collateral
    # max_debt_quantity: The maximum quantity of debt that can remain in the CDP
    # max_debt_ratio: The maximum debt ratio that can remain in the CDP
    def set_sell_curve(max_sell_price, max_debt_quantity, max_debt_ratio):
        pass