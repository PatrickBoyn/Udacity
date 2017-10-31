import os

direct = os.getcwd()

def renamer():
	table = str.maketrans(dict.fromkeys('0123456789'))
	# this will not work unless it is converted to a string
	# TODO: find a way of changing the directory for this to work
	file_names = str(os.listdir(r'C:\Users\dakil\Desktop\Udacity\Renamer\prank'))
	for lists in file_names:
		os.rename(file_names, file_names.translate(table))
End of function
os.chdir(r'C:\Users\dakil\Desktop\Udacity\Renamer\prank')
print(direct)
renamer()		
