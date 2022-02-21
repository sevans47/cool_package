from unittest.util import three_way_cmp
from cool_package.lib import try_me

def test_try_me():
    secret_message = try_me()
    assert secret_message == "Thanks for being cool!"
