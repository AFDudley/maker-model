class ParameterDB:

    def __init__(self):
        # TODO - these values should be read from a config file
        self.collaterization = {'BTC':  1.5,
                                'ETH':  1.5}
        self.margin_cutoff = {'BTC':  1.5,
                              'ETH':  1.5}
        self.interest_rate = 1.02
