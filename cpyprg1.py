from prg1 import To_do_list

ma=To_do_list("work")
while True:
	s=input("enter the choice: \n \
		1. Add to tasks\n \
		2. Mark Done \n \
		3. See tasks \n \
		4. Exit")

	if s == 1:
		ma.add()	

	elif s == 2:
		ma.mark_done()

	elif s == 3:
		ma.see_tasks()

	else:
		break
	
	
	
