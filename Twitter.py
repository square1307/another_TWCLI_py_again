# -*- coding: utf-8 -*-
import auth
import json
from requests_oauthlib import OAuth1Session

class CLI_Twitter:
	def __init__(self):
		self.twitter = OAuth1Session(auth.API_key,auth.API_secret_key,auth.Access_token,auth.Access_token_secret)
		
	def getHomeTimeLines(self,intCount=10):
		url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'

		params = {'count':intCount}
		res = self.twitter.get(url, params = params)

		if res.status_code == 200:
			jsonTimelines = json.loads(res.text)
			return jsonTimelines
		else:
			print("Failed with error code:%d" % res.status_code)
			return []

	def getUserTimeLines(self,strScreenName,intCount=10):
		url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
		
		params = {'screen_name':strScreenName, 'count': intCount}
		res = self.twitter.get(url, params = params)
		if res.status_code == 200:
			jsonTimelines = json.loads(res.text)
			return jsonTimelines
		else:
			print("Failed with error code:%d" % res.status_code)
			return []
	
	def searchUser(self,strUsername,intCount=10):
		url = 'https://api.twitter.com/1.1/users/search.json'
		
		params = {'q':strUsername, 'count':intCount}
		res = self.twitter.get(url, params = params)
		if res.status_code == 200:
			jsonUserData = json.loads(res.text)
			return jsonUserData
		else:
			print("Failed with error code:%d" % res.status_code)
			return []