import requests
import bs4

comedy = "https://en.wikipedia.org/wiki/Golden_Globe_Award_for_Best_Motion_Picture_%E2%80%93_Musical_or_Comedy"
director = "https://en.wikipedia.org/wiki/Golden_Globe_Award_for_Best_Director"

d = requests.get(comedy)
soup = bs4.BeautifulSoup(d.text, "html.parser")
tables = soup.select(".wikitable")
pt = {}
for table in tables:
	year = ""
	for row in table.find_all('tr')[1:]:
		fields = row.find_all('a', title=True)
		if len(fields) == 1:
			continue
		if 'Golden Globe Awards' in fields[0].attrs['title'] or fields[0].text in ['1951', '1954', '1955']:
			year = fields[0].text
			pt[year] = [(fields[1].text+"*", fields[2].text)]
		else:
			pt[year].append( (fields[0].text, fields[1].text) )



d2 = requests.get(director)
soup2 = bs4.BeautifulSoup(d2.text, "html.parser")
tables2 = soup2.select(".wikitable")
pt2 = {}
for table in tables2:
	year = ""
	for row in table.find_all('tr')[1:]:
		fields = row.find_all('a', title=True)
		if len(fields) == 1:
			continue
		if 'Golden Globe Awards' in fields[0].attrs['title'] or fields[0].text in ['1951', '1954', '1955']:
			year = fields[0].text
			pt2[year] = [(fields[2].text, fields[1].text)]
		else:
			pt2[year].append( (fields[1].text, fields[0].text) )
res = {}			
for year in pt:
	for tup in pt[year]:
		for tup2 in pt2[year]:
			if tup2[0] in tup[0]:
				if year not in res:
					res[year] = [tup]
				else:
					res[year].append(tup)


import pprint
pprint.pprint(res)			
print "{}/{}".format(len(res), len(pt))
