IP= ''
PORT = 8888

HEADER_SIZE = 9
REQ = 0
SUCC = 1
FAIL = 2

class Header(object):
	msgLen = ""
	msgCode = ""
	msgRslt = ""

	def __init__(self):
		pass

	def setData(self, buf):
		self.msgLen = buf[0:4].strip('\0')
		self.msgCode = buf[4:8].strip('\0')
		self.msgRslt = buf[8:9].strip('\0')
		return

	def setMsgLen(msgLen):
		self.msgLen = msgLen
		return
	def setMsgCode(msgCode):
		self.msgCode = msgCode
		return
	def setMsgRslt(self, rslt):
		self.msgRslt = rslt
		return

class Bind(Header):
	customID = ""
	customPW = ""

	def __init__(self):
		pass

	def respondBind(self, buf):
		super(Bind, self).setData(buf)
		self.customID = buf[9:29].strip('\0')
		self.customPW = buf[29:49].strip('\0')
		return
		
	def checkCustom(self):
		if self.customID == "jino" and self.customPW == "pwjino":
			return 0
		else :
			return 1
		return 0

class BindAck(Header):
	failCause=""

	def __init__(self):
		pass

	def makeRetBindAck(self, opt):
		buf=""
		if opt == SUCC :
			buf = "12".ljust(4,'\0')
			buf += "S000".ljust(4,'\0')
			buf += "1"
			buf += "0000".ljust(4,'\0')
		return buf

class MO(Header):
	seqNum=""
	rDate=""
	orgAddr=""
	dstAddr=""
	callbackNo=""
	srcType=""
	msg=""
	def __init__(self):
		pass

	def makeReqMO(self):
		msgLen = 0
		seqNum = "AABBCCDDEE0011223344".ljust(20,'\0')
		msgLen += 20
		rDate = "20180716153123592".ljust(17,'\0')
		msgLen += 17
		orgAddr = "01012345678".ljust(32, '\0')
		msgLen += 32
		desAddr = "18112180".ljust(32, '\0')
		msgLen += 32
		callbackNo = "01012341234".ljust(32, '\0')
		msgLen += 32
		strType = "1".ljust(1, '\0')
		msgLen += 1
		msg = "Mo msg"
		msgLen += len(msg)

		super(MO, self).setMsgLen(msgLen)
		super(MO, self).setMsgCode("Q1000")
		super(MO, self).setMsgRslt(REQ)
		return

	def buildMOMsg(self):
		return
