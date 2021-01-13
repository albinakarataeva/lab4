import requests
import json


def DoRequest(method, cmd="", data=""):
	try:
		url = 'http://localhost:8080/cgi-bin/WEBClient.py'
		header = {"Content-type": 'text/html'}
		res = method(url+cmd, headers=header, data=json.dumps(data))
		if res.status_code == 200:
			print(res.content)
			return json.loads(res.content)
	except Exception as ex:
		print(ex)


def GetList(id):
	q = '?console=1&ClientID=' + str(id)
	res = DoRequest(requests.get, q)
	return res

def SendMsg(clientId, message, id):
	q = '?'
	q += 'id='+ str(id)
	q += '&message='+ message
	q += '&console=' + '1'
	q += '&ClientID=' + str(clientId)
	res = DoRequest(requests.get, q)

def Exit(id):
	q = '?console=1&ClientID=' + str(id) + 'exit=1'
	res = DoRequest(requests.get, q)

def Init():
	q = '?console=1&' + 'init=1'
	res = DoRequest(requests.get, q)
	return res