class ParameterDB:

    def __init__(self):
        # TODO - these values should be read from a config file
        self.volatility_class = {'btc':         'standard',
                                 'ether':       'standard',
                                 'dgxgold':     'standard',
                                 'makercoin':   'high risk',
                                 'augur rep':   'high risk'}
        self.collaterization = {'standard':     1.5,
                                'high risk':    2}
        self.margin_cutoff = {'standard':   1.2,
                              'high risk':  1.5}
