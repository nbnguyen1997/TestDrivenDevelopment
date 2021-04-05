import unittest
from datetime import datetime
from unittest import mock
from ..action import PrintAction
from ..alert import Alert
from ..rule import PriceRule
from ..stock import Stock
# mock.patch.TEST_PREFIX="test_executing"

class PrintActionTest(unittest.TestCase):
    @mock.patch("builtins.print") 
    def test_executing_action_prints_message(self,mock_print):    
        action = PrintAction()
        action.execute("GOOG > $10")
        mock_print.assert_called_with("GOOG > $10")

    def test_action_doesnt_fire_if_rule_doesnt_match(self) :
        goog = Stock("GOOG")
        exchange = {"GOOG":goog}
        rule = PriceRule("GOOG",lambda stock:stock.price>10)
        rule_spy = mock.MagicMock(wraps=rule)
        action = mock.MagicMock()
        alert = Alert("sample alert", rule_spy, action)
        alert.connect(exchange)
        alert.check_rule(goog)
        rule_spy.matches.assert_called_with(exchange)
        self.assertFalse(action.execute.called)
    
    def test_action_fires_when_rule_matches(self):
        goog = Stock("GOOG")
        exchange = {"GOOG": goog}
        rule = mock.MagicMock()
        rule.matches.return_value = True
        rule.depends_on.return_value = {"GOOG"}
        action = mock.MagicMock()
        alert = Alert("sample alert", rule, action)
        alert.connect(exchange)
        goog.update(datetime(2014, 5, 14), 11)
        rule.matches.assert_called_with(exchange)
        self.assertTrue(action.execute.called)