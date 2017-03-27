#!/usr/bin/env python3
# coding: utf-8
import math
import json


BASE_URL = "https://citymapper.com/"
ENDPOINT = "api/7/journeys?start=FROM&end=TO&region_id=fr-paris"


def f_minutes(seconds):
    """Simply formats time(int) to minutes, rounding to ceil

    :param seconds The value to format in seconds

    :type seconds int

    :returns: The value of seconds formatted in seconds
    :rtype int

    """
    val = math.ceil(seconds / 60)
    return val


def make_url(source, destination):
    """Returns the formatted url for the request

    :param source The `from` location of the journey
    :param destination The `to` location of the journey (actual destination)

    :type source str
    :type destination str

    :return: the formatted URL to use for the request to the Citymapper API
    :rtype str

    """
    unformatted_url = BASE_URL + ENDPOINT
    formatted = unformatted_url.replace(
            "FROM", source).replace("TO", destination)
    return formatted


def dt_to_s(s_time):
    """TODO: Simple function parsing a basic timestamp

    :param s_time The string to parse

    :type s_time str

    :returns: tuple of reformatted strings, as date and hour
    :rtype str, str

    """
    try:  # Of course I hard coded these value. -> no need to import datetime
        year = s_time[:4]
        month = s_time[5:7]
        day = s_time[8:10]
        hour = s_time[11:13]
        minute = s_time[14:16]
        seconds = s_time[17:19]
        date = "%s/%s/%s" % (year, month, day)
        date_hours = "%s:%s:%s" % (hour, minute, seconds)
        return date, date_hours
    except IndexError:
        return s_time, None


def content_to_obj(content):
    """Transforms the url's content to JSON object

    :param content The content of the page

    :type content str

    :returns: a JSON object containing the journeys
    :rtype JSON

    """
    obj = json.loads(content)
    return obj
