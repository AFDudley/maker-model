class CDP:

    next_id = 0
    env = None

    def __init__(self, env, collateral_type):
        self._id = CDP.next_id
        CDP.next_id += 1
        if not CDP.env:
            CDP.env = env
        self.owner = env.actor
        self.created_timestamp = 0

        self.collateral_type = collateral_type
        self.collateral_bal = CDP.env.balances[self.collateral_type]
        self.principal_debt = 0
        self.interest_debt = 0

    def _has_sufficient_collateral(self, dai, collateral):
        collaterization = CDP.env.params.collaterization[self.collateral_type]
        price_idx = CDP.env.feeds["SDR/" + self.collateral_type]
        return dai < (price_idx * collateral) / collaterization

    def _is_owner(self):
        if CDP.env.actor != self.owner:
            raise ValueError("%s can't issue from cdp owned by %s"
                             % (CDP.env.actor, self.owner))

    def collateral_quantity(self):
        return self.collateral_bal.get(self.collateral_type)

    def add_collateral(self, quantity):
        self.collateral_bal.send(CDP.env.actor, self._id, quantity)

    def free_collateral(self, quantity):
        self._is_owner()
        balance = self.collateral_bal.get(self._id)
        debt = self.principal_debt + self.interest_debt
        if not self._has_sufficient_collateral(debt, balance - quantity):
            raise ValueError("Insufficient free collateral")
        self.collateral_bal.send(self._id, self.owner, quantity)

    def issue(self, dai_quantity):
        self._is_owner()
        balance = self.collateral_bal.get(self._id)
        if not self._has_sufficient_collateral(dai_quantity, balance):
            raise ValueError("Insufficient collateral to issue %d dai",
                             dai_quantity)
        self.created_timestamp = CDP.env.time
        self.principal_debt = dai_quantity
        CDP.env.balances["DAI"].add(CDP.env.actor, dai_quantity)

    def cover(self, dai_quantity):
        # ensure sender is owner
        pass

    def bailout(self):
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

class CDPEngine:

    def __init__(self, parameterdb, feeddb):
        self.parameterdb = parameterdb
        self.feeddb = feeddb
        self.cdp_list = []

    def buy_cdp(self, owner, collateral_type, collateral_amount):
        """This method gives the buyer right to a CDP and issues Dai.

        Return:
            The amount of Dai issued.
        """
        volatility_class = self.parameterdb.volatility_class[collateral_type]
        collaterization = self.parameterdb.collaterization[volatility_class]
        price_idx = self.feeddb.get_index(collateral_type)
        debt = (price_idx * collateral_amount) / collaterization
        new_cdp = CDP(owner, debt, collateral_type,
                      collateral_amount, volatility_class)
        self.cdp_list.append(new_cdp)
        return debt

    def get_margin_callable_cdps(self):
        """Get a list of all CDP's that are below the margin cutoff.

        Return:
            A list of id's for the CDP's.
        """
        cutoff_list = []
        for i, cdp in enumerate(self.cdp_list):
            price_idx = self.feeddb.asset_index[cdp.collateral_type]
            collateral = (price_idx * cdp.collateral_amount)
            margin = self.parameterdb.margin_cutoff[cdp.volatility_class]
            # TODO - this should take inflation into account
            if collateral/cdp.initial_debt < margin:
                cutoff_list.append(i)
