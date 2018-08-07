#-*- encoidng=utf-8 -*-

__name__='__main__'

class Client :
	userID=""
	userPW=""
	def __init__(self):
		return
	def setClientInfo(self, userID, userPW):
		self.userID = userID
		self.userPW = userPW
		return


def main ():

	userID = raw_input("아이디 : ")
	userPW = raw_input("비밀번호 : ")

	c = Client()
	c.setClientInfo(userID, userPW)

	return

if __name__ == '__main__':
	main()
