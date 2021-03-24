import unittest
from unittest import mock

from ..email_action import EmailAction

@mock.patch("smtplib.SMTP")
class EmailActionTest(unittest.TestCase):
    def setUp(self) :
        self.action = EmailAction(to="siddarta@silvertripesoftware.com")

    def test_email_is_send_to_the_right_ser(self,mock_smtp_class):
        self.action.execute("MSFT has crossed $10 price level")
        mock_smtp_class.assert_called_with("email.stocks.com")

    def test_connection_closed_after_sending_mail(self,mock_smtp_class):
        mock_smtp =mock_smtp_class.return_value
        self.action.execute("MSFT has crossed $10 price level")
        mock_smtp.send_message.assert_called_with(mock.ANY)
        self.assertTrue(mock_smtp.quit.called)
        mock_smtp.assert_has_calls([
            mock.call.send_message(mock.ANY),
            mock.call.quit()])