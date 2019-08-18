from bitshares.utils import assets_from_string


def test_assets_from_string():
    assert assets_from_string('USD:X4T') == ['USD', 'X4T']
    assert assets_from_string('X4TBOTS.S1:X4T') == ['X4TBOTS.S1', 'X4T']
