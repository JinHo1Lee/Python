# -*- coding: utf8 -*-

from socket import *
from select import *
import sys
from time import ctime
from bind import *

__name__ = "__main__"


class KCTServer:
	def __init__(self):
		return	

	def setSocket (self, ip, port):
		self.serverSocket = socket(AF_INET, SOCK_STREAM)

		ADDR = (ip, port)
		self.serverSocket.bind(ADDR)

		self.serverSocket.listen(10)
		self.connection_list = [self.serverSocket]
		return

	def getPacket(self, sock):
		buf = ""
		msglen = 0

		buf = sock.recv(HEADER_SIZE)
		if buf:
			msglen = int(buf[0:4].strip('\0')) - HEADER_SIZE
			if msglen > 0:
				buf += ((sock.recv(msglen)))
			else :
				return ""
		else:
			return "";
		return buf

	def processMsg(self, buf):
		code = buf[4:8].strip('\0')
		if code == "Q000":
			self.processBind(buf)

		return

	def processBind(self, buf):
		bind = Bind()
		bindAck = BindAck()

		bind.respondBind(buf)

		if bind.checkCustom() == 0 :
			print "Bind Succ"
			buf = bindAck.makeRetBindAck(SUCC)
			self.clientSocket.send(buf)
		else:
			print "Bind Fail"
		return

	def run(self):
		while self.connection_list:
			try:
				read_socket, write_socket, error_socket = select(self.connection_list, [], [], 10)

				for sock in read_socket:
					if sock == self.serverSocket:
						self.clientSocket, addr_info = self.serverSocket.accept()
						self.connection_list.append(self.clientSocket)
					else:
						buf = self.getPacket(sock)
						if buf:
							self.processMsg(buf)
						else :
							print "Client Socket Close"
							self.connection_list.remove(sock)
							sock.close()
			except KeyboardInterrupt:
				self.serverSocket.close()
				sys.exit()
		return

def main():
	server = KCTServer()

	server.setSocket(IP, PORT)

	server.run()

	return


if __name__ == "__main__":
	main()

