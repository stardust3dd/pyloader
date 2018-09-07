from bs4 import BeautifulSoup
import requests, wget
import urllib.request

url= input("Enter url: "); page=requests.get(url); data= page.text
soup= BeautifulSoup(data, 'lxml'); op= open('dl.txt', 'w')

links= soup.find_all('a'); links.pop(0)
for i in links:
	link= i.get('href'); link= url+link
	print(link)
	op.write(link+'\n')
