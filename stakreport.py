import requests
import bs4

hosts = ['192.168.1.104:1001', '192.168.1.90:1001']

res = {}
for host in hosts:
	data = requests.get("http://"+host+"/h")
	soup = bs4.BeautifulSoup(data.text, "html.parser")
	res[host] = {}
	for row in soup.findAll('tr'):
		th = row.findAll('th')[0].text.strip()
		if 'Thread' in th:
			continue
		tds = row.findAll('td')
		tds = [float(td.text.strip()) for td in tds if len(td.text) > 0 ]
		res[host][th] = tds

totals = [0,0,0]
for host in res:
	for i,val in enumerate(res[host]['Totals:']):
		totals[i] += val

print "Totals: {}".format(totals)
