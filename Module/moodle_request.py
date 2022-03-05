import os
from bs4 import BeautifulSoup
import requests


headers = {"usre-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36"}


class request_moodle():
	def __init__(self):
		self.s = requests.Session()
		return

	def connection(self , username : str , password : str):
		login_data = {
		'username': username,
		'password': password,
		'_eventId': 'submit'
		}
		url = "https://cas.univ-lille.fr/login?service=https%3A%2F%2Fmoodle.univ-lille.fr%2Flogin%2Findex.php%3FauthCAS%3DCAS"
		request = self.s
		src = request.get(url,headers=headers).content
		soup = BeautifulSoup(src,'html.parser')
		login_data['execution'] = soup.find_all("input" , attrs={'name' : 'execution'})[0]["value"]
		request.post(url , data = login_data , headers = headers)
		return 

	def get_all_classes(self ):
		classes=[]
		url_t = 'https://moodle.univ-lille.fr/course/index.php?categoryid=2137'
		request = self.s
		src = request.get(url_t,headers=headers).content
		soup = BeautifulSoup(src,'html.parser')
		data=[]
		test = soup.find_all("a")

		for i in test:
			if i.attrs.get('href') and 'https://moodle.univ-lille.fr/course/view.php?id=' in i.attrs['href']:
				if i.attrs.get("role") and 'menuitem' in i.attrs["role"]:
					data.append({'title': i.attrs["title"],
					'link': i.attrs["href"]})
		return data

	def get_work_to_do(self):
		request = self.s
		url="https://moodle.univ-lille.fr/my/"
		data=[]
		src = request.get(url,headers=headers).content
		soup = BeautifulSoup(src,'html.parser')
		temp = soup.find_all("a")
		dic_temp={}
		for i in temp:
			
			if i.attrs.get("data-type") and "event" in i.attrs["data-type"]:
				dic_temp['title']=i.text[:-19]
				dic_temp['link']=i.attrs["href"]
			if i.attrs.get('href') and "https://moodle.univ-lille.fr/calendar/view.php?view=day&time=" in i.attrs["href"]:
				dic_temp['date']=i.text.split(" ")
			if dic_temp!={} and dic_temp.get('date'):
				data.append(dic_temp)
				dic_temp={}
		return data

	def get_EDT(self):
		img=[]
		request = self.s
		url="https://moodle.univ-lille.fr/course/view.php?id=28355"
		src=request.get(url,headers=headers)
		temp=BeautifulSoup(src.content,'html.parser').find_all("a")
		for i in temp:
			if "EPDT" in i.text:
				edt=i.attrs["href"]
		temp_edt = request.get(edt,headers=headers)
		temp_edt_1=BeautifulSoup(temp_edt.content,'html.parser').find_all("img")
		for i in temp_edt_1:
			if "class" in i.attrs.keys():
				if i.attrs["class"] == ['resourceimage']:
					return i.attrs['src']
		

	def img_downloader(self,url: str,PATH : str):
		request = self.s
		img_data = request.get(url).content
		with open(PATH +"/"+ "EDT.png", "wb") as handler:
		    handler.write(img_data)
		return PATH