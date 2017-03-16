import climapper


ENDPOINT = "api/7/journeys?start=FROM&end=TO&region_id=fr-paris"


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
    base_url = "https://citymapper.com/api/7/journeys?"
    end_url = "end=48.928378%2C2.162200&region_id=fr-paris"
    valid_url = base_url + "start=48.813896%2C2.392448&" + end_url
    assert url == valid_url


def test_get_params_simple():
    src_exp = "48.813896%2C2.392448"
    dst_exp = "48.928378%2C2.162200"
    src, dest = climapper.get_params()
    assert src_exp == src
    assert dst_exp == dest


def test_dt_to_s():
    date_str = "1994-01-01 18:32:18.299"
    date_exp, hour_exp = climapper.dt_to_s(date_str)
    assert "1994/01/01" == date_exp
    assert "18:32:18" == hour_exp


def test_manage_distance():
    base_dict = dict()
    correct_ele = {'distance': 1240}
    resp_dict = {'distance_meters': 1240}
    climapper.manage_distance(resp_dict, base_dict)
    assert correct_ele == base_dict
