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
    assert correct_ele['distance'] == base_dict['distance']


def test_content_to_obj():
    base_string = '{"test":true, "Should": "Be True"}'
    valid_obj = {"test": True, "Should": "Be True"}
    base_obj = climapper.content_to_obj(base_string)
    assert base_obj == valid_obj


def test_manage_date_ignore_date():
    base_depart = "1994-01-01 18:32:18.299"
    base_arrive = "1994-11-21 19:33:29.299"
    test_dict = dict()
    valid_dict = dict()
    base_dict = {
            "departure_time": base_depart,
            "arrival_time": base_arrive
            }

    valid_dict['start_hour'] = '18:32:18'
    valid_dict['end_hour'] = '19:33:29'
    climapper.manage_date(base_dict, test_dict)
    assert test_dict == valid_dict


def test_manage_date_dont_ignore_date():
    base_depart = "1994-01-01 18:32:18.299"
    base_arrive = "1994-11-21 19:33:29.299"
    test_dict = dict()
    valid_dict = dict()
    base_dict = {
            "departure_time": base_depart,
            "arrival_time": base_arrive
            }

    valid_dict['start_hour'] = '18:32:18'
    valid_dict['end_hour'] = '19:33:29'
    valid_dict['start_date'] = '1994/01/01'
    valid_dict['end_date'] = '1994/11/21'
    climapper.IGNORE_DATE = False
    climapper.manage_date(base_dict, test_dict)
    assert test_dict == valid_dict
