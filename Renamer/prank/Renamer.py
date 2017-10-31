import os



def renamer():
	table = str.maketrans(dict.fromkeys('0123456789'))
	file_names = os.listdir(r'C:\Users\dakil\Desktop\Udacity\Renamer\prank')
	print(file_names)
	for items in file_names:
		os.rename(items, items.translate(table))

# End of function

renamer()		
