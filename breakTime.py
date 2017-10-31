import webbrowser
import time

''' I found time module simply by googling sleep
	this is my code other than finding the syntax
	for using time with Python I am familiar with C#, 
	and it has a similar built in bit of code(thread.sleep), 
	and I reasoned that Python must as well. I found something and found a 
	time.sleep on the first link and used auto complete to figure the rest
	I have sublime 3 set up with a really nice auto complete'''

'''The for loop idea of using range I found on stack overflow Just google 
   'looping multiple times in python', and it's one of the first to show
   really the only thing I got from the article was hmm, they used range that way?
   Why not try it. I know about for loops in Python (they're the equivelant of a C# foreach), 
   I just havne't used them this way before. Range uses a start and stop, 
   and one other paramater I don't recall if you do just one param, 
   it's the number you stop at'''

print('The program started on ' + time.ctime())

def time_out():
	for i in range(4):
		time.sleep(5)
		webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")

time_out()