class To_do_list(object):

	def __init__(self,list_name):
		self.list_name=list_name
		self.to_do=[]
		self.done=[]

	def add(self):
		x=raw_input("enter task:")
		self.to_do.append(x)
			
	def mark_done(self):
		y=raw_input("enter the done work:")
		if y in self.to_do:
			self.done.append(y)
		self.to_do.remove(y)
		
	def see_tasks(self):
		print(self.to_do)
		print(self.done)

