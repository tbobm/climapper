import climapper


def test_f_minutes_big():
    """TODO: Docstring for test_.

    :arg1: TODO
    :returns: TODO

    """
    res = climapper.f_minutes(300)
    assert res == 5


def test_f_minutes_with_round():
    res = climapper.f_minutes(289)
    assert res == 5
