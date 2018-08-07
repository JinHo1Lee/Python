
class A:
	data1=0
	data2=0
	def setData(self, *data):
		self.data1 = data[0]
		self.data2 = data[1]
		return
	def printdata(self):
		print "data1 : %d, data2: %d" %(self.data1, self.data2)
		return;
		


def main ():
	a = A();

	a.setData(1, 2)
	a.printdata()
	return

main()
