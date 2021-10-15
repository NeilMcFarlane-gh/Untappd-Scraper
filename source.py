# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 10:44:25 2021

@author: Neil McFarlane
"""


import requests

from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from selenium import webdriver


def get_data_from_untappd(url):
    # Setting up and Making the Web Call
    try:
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'
        headers = {'User-Agent': user_agent}
        # Make web request for that URL and don't verify SSL/TLS certs
        response = requests.get(url, headers=headers, verify=False)
        return response.text

    except Exception as e:
        print('[!]   ERROR - Untappd issue: {}'.format(str(e)))
        exit(1)

def get_user_data(passed_user):
    # Parsing user information
    url = 'https://untappd.com/user/{}/beers'.format(passed_user)
    print("\n[ ] USER DATA: Requesting {}".format(url))
    resp = get_data_from_untappd(url)
    html_doc = BeautifulSoup(resp, 'html.parser')
    with open('test', 'w', encoding='utf-8') as F:
        F.write(str(html_doc))
    user1 = html_doc.find_all('span', 'stat')
    if user1:
        return user1
    
get_user_data('p0rkyP')