class Test1:
	def a1(self):
		aa = 'Aish'
		print aa
	
	def tuplefun(self):
		#Tuples in python
		tuple=('rahul',100,60.4,'deepak')
		tuple1=('sanjay',10) 
		print tuple
		print tuple[2:]
		print tuple[1:]
		print tuple1[0]
		print tuple+tuple1 

	def leapyr(self):
		year = 2000
		if year%4==0:
			print "Leap Year"
		else:
			print "Not a Leap Year"

class Test2:
	def a2(self):	
		number = 2	
		for a in range(1,6):
			print number * a


def main():	
	Test1.a1()
	
if __name__ == '__main__':
    main()