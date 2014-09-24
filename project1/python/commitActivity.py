#!/usr/bin

import requests, json, sys, time, re, pickle, codecs
import bs4 as BeautifulSoup

URL = 'https://api.bitbucket.org/2.0/repositories'
r = requests.get(URL)
json_obj = json.loads(r.text)

values = json_obj['values']
links = values['links']
print links
