#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import unidecode
import requests
import lxml.html as lxml_html
from StringIO import StringIO

def fetch_data(remote_url):
	try:
		response = requests.get(remote_url)
	except:
		return None
	html_parsed = lxml_html.parse(StringIO(response.content))

	usersData = []
	for table in html_parsed.iter('table'):
		fields = []
		if table.attrib.has_key('class') and table.attrib['class'] == 'dataTable':
			for tr in table.iter('tr'):
				if tr.attrib.has_key('class') and tr.attrib['class'] == 'tableHeader':
					for td in tr.iter('td'):
						field_name = unidecode.unidecode(td.text_content().strip(' \t\n\r')).lower()
						fields.append(re.sub(r'\W+','-',field_name))
						# nazivi polja
				else:
					userData = {}
					for i, td in enumerate(tr.iter('td')):
						if not td.attrib.has_key('class') or td.attrib['class'] != 'navBar':
							userData[fields[i]] = td.text_content().strip(' \t\n\r')
						# podaci
					if len(userData) > 0:
						usersData.append(userData)
	return usersData

def save_data(usersData):
	print 'fo: %i' % len(usersData['fo']) # ispis broja duznika fizickih osoba
	print usersData['fo'][123]
	print 'po: %i' % len(usersData['po']) # ispis broja duznika pravnih osoba
	print 'gr: %i' % len(usersData['gr']) # ispis broja duznika gradjana
	# ovdje upisi podatke u bazu na koji god nacin zelis, sve je u userData varijabli

if __name__ == "__main__":
	
	data = { 'fo': [], 'po': [], 'gr': [] }
	
	for data_type in data.keys():
		for i in range(1, 2000):
			temp = fetch_data('http://duznici.porezna-uprava.hr/%s/svi/%i.html' % (data_type, i))
			if len(temp) == 0: 
				break
			else: 
				if temp is not None:
					data[data_type] += temp

	save_data(data)