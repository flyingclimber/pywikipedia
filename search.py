#!/usr/bin/python

'''

    search - Simple Wikipedia Search

    Copyright (C) 2014, Tomasz Finc <tomasz@gmail.com>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

'''

import urllib
import json
import argparse

PARSER = argparse.ArgumentParser(description='Wikipedia lookup tool')

PARSER.add_argument('-s', '--search', help='search')
PARSER.add_argument('-l', '--lang', help='lang', default='en')

ARGS = PARSER.parse_args()

PROTO = 'https://'
DOMAIN = 'wikipedia.org'
LANG = ARGS.lang
PATH = '/w/'
APIPHP = 'api.php?'

ACTION = 'opensearch'
FORMAT = 'json'
SEARCH = ARGS.search
LIMIT = '25'
NAMESPACE = '0'

BASE = PROTO + LANG + "." + DOMAIN + PATH + APIPHP

PARAMS = urllib.urlencode({'action': ACTION, 'format': FORMAT,
                         'search': SEARCH, 'limit': LIMIT,
                         'namespace': NAMESPACE})

URLRESP = urllib.urlopen(BASE, PARAMS)
SEARCH_RESP = URLRESP.read()
JSON = json.loads(SEARCH_RESP)

num = 1

for i in JSON[1]:
    print "%i: %s" % (num, repr(i).decode("unicode-escape"))
    num += 1
