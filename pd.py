#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from os import path

current_dir = path.dirname(path.realpath(__file__))
sys.path.append(path.join(current_dir, path.pardir))

import requests
import lxml.html as lxml_html
from StringIO import StringIO

def save_data(remote_url):
	response = requests.get(remote_url)
	html_parsed = lxml_html.parse(StringIO(response.content))

	usersData = []
	for table in html_parsed.iter('table'):
		fields = []
		if table.attrib.has_key('class') and table.attrib['class'] == 'dataTable':
			for tr in table.iter('tr'):
				if tr.attrib.has_key('class') and tr.attrib['class'] == 'tableHeader':
					for td in tr.iter('td'):
						fields.append(td.text_content().strip(' \t\n\r'))
						# nazivi polja
				else:
					userData = {}
					for i, td in enumerate(tr.iter('td')):
						userData[fields[i]] = td.text_content().strip(' \t\n\r')
						# podaci
					usersData.append(userData)
	#print usersData
	# ovdje upisi podatke u bazu na koji god nacin zelis, sve je u userData varijabli

if __name__ == "__main__":
    save_data('http://duznici.porezna-uprava.hr/fo/svi/1.html')
    # ovdje naslazi ostale stranice ili sliozi neki drugi algoritam kako ces prolazit kroz stranice