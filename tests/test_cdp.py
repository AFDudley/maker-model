import pytest
from model.cdp import CDP
from model.environment import Environment

class TestCDP:

    def setup_class(self):
        self.env = Environment()
        self.env.feeds["SDR/ETH"] = 0.67

    def setup_method(self, metod):
        self.env.actor = 'usr1'
        self.cdp = CDP(self.env, "ETH")

    def test_issue_wrong_actor(self):
        self.env.actor = 'usr2'
        with pytest.raises(ValueError):
            self.cdp.issue(100)

    def test_issue_too_much(self):
        with pytest.raises(ValueError):
            self.cdp.issue(100)

    def test_issue_correct_amount(self):
        self.env.balances["ETH"].add(self.env.actor, 224)
        self.cdp.add_collateral(224)
        self.cdp.issue(100)
        dai_balance = self.env.balances["DAI"].get(self.env.actor)
        assert(dai_balance == 100)

    def test_free_collateral(self):
        self.env.balances["ETH"].add(self.cdp._id, 999)
        self.cdp.issue(200)
        with pytest.raises(ValueError):
            self.cdp.free_collateral(999)
        self.cdp.free_collateral(200)
        eth_balance = self.env.balances["ETH"].get(self.env.actor)
        assert(eth_balance == 200)

    def test_cover(self):
        self.env.balances["DAI"]._balances[self.env.actor] = 100
        self.env.balances["ETH"]._balances[self.env.actor] = 0
        self.env.balances["ETH"].add(self.cdp._id, 200)
        self.cdp.principal_debt = 90
        self.cdp.interest_debt = 10

        self.cdp.cover()

        assert(self.env.balances["DAI"].get(self.env.actor) == 0)
        assert(self.env.balances["DAI"].get(self.env.maker_addr) ==
               self.cdp.interest_debt)
        assert(self.env.balances["ETH"].get(self.cdp._id) == 0)
        assert(self.env.balances["ETH"].get(self.env.actor) == 200)
