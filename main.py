import Twitter
import printData

twitter = Twitter.CLI_Twitter()

dictOptions = {
'h':'home timeline\n	  [OPTION] [COUNT(DEFAULT 10)]',
'su':'search user\n	  [OPTIONS] [*KEYWORD] [COUNT(DEFAULT 10)]',
'ut':'user timeline\n	  [OPTION] [*USERID] [COUNT(DEFAULT 10)]'
}

def helpMessage():
	strOutput = ""
	for option in dictOptions:
		print("{}	= {}".format(option,dictOptions[option]))
	strOutput = input()
	return strOutput

if __name__ == '__main__':
	strInput = helpMessage()
	while strInput != "q":
		if strInput != "":
			arrInput = strInput.split(" ")
		strArgs = arrInput[0]
		arrArglist = arrInput[1:]
		
		try:
			if strArgs == 'h':
				printData.printTimelines(twitter.getHomeTimeLines(*arrArglist))
			elif strArgs == 'su':
				printData.printUsers(twitter.searchUser(*arrArglist))
			elif strArgs == 'ut':
				printData.printTimelines(twitter.getUserTimeLines(*arrArglist))
			elif strArgs =='q':
				exit()
			
		except Exception as e:
			print(str(e))
		strInput = input()
		
