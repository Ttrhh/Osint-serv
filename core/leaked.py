import requests, json, re

class leaked:

	def hash(self, hash):
		text = requests.get("https://hashtoolkit.com/reverse-hash/?hash="+hash).text
		passw = re.findall(r"/generate-hash/\?text=(.*?)\"", text)
		
		if len(passw) != 0:
			passw = passw[0]
		else:
			passw = None

		return(passw)

	def email(self, email):
		dataList = []

		try:
			req = requests.get("https://haveibeenpwned.com/api/v2/breachedaccount/"+email, headers={"Content-Type":"application/json", "Accept":"application/json"})
			status = req.status_code

			if status_code == 200:
				data = json.loads(req.text)
				count = len(data)

				for d in data:
					name = d['title']
					domain = d['domain']
					date = d['BreachDate']

					dataDic = {'Title':name, 'Domain':domain, 'Date':date}
					dataList.append(dataDic)
				
				return(dataList)

		except:
			return(None)