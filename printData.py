

def printTimelines(jsonTimelines):
	for objTweet in jsonTimelines:
		print(objTweet['user']['name']+":")
		print(objTweet['text'])
		print("Tweet at:{}".format(objTweet['created_at']))
		print("=============================================")
		
		
def printUsers(jsonUserData):
	for objUser in jsonUserData:
		print("{}:{}".format(objUser['screen_name'],objUser['name']), end='')
		print("[FOLLOWING]" if objUser['following'] else "",end='')
		print("[FOLLOWED]" if objUser['followed_by'] else "",end='')
		print()