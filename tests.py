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


def test_make_url():
    url = climapper.make_url("48.813896%2C2.392448", "48.928378%2C2.162200")
    valid_url = "https://citymapper.com/api/7/journeys?start=48.813896%2C2.392448&end=48.928378%2C2.162200&region_id=fr-paris"
    assert url == valid_url
