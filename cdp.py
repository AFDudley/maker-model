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


class CDP:

    def __init__(self, owner, debt, collateral_type,
                 collateral_amount, volatility_class):
        self.owner = owner
        self.initial_debt = debt
        self.collateral_type = collateral_type
        self.collateral_amount = collateral_amount
        self.volatility_class = volatility_class

    def transfer(self, new_owner):
        self.owner = new_owner
