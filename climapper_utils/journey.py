#!/usr/bin/env python3
# coding: utf-8
import requests
import unidecode


BASE_H = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0)"
SPEC_H = " Gecko/20100101 Firefox/32.0"
USER_AGENT = BASE_H + SPEC_H
HEADERS = {'user-agent': USER_AGENT}


def make_request(url):
    """
    Requests the content of the formatted url
    and returns the content of the page

    :param url The url with the `GET` parameters embedded in

    :type url str

    :returns: content of the url request
    :rtype str

    """
    try:
        response = requests.get(url, headers=HEADERS)
    except Exception as e:
        raise e
    content = response.content
    return unidecode.unidecode(content.decode('utf-8'))

