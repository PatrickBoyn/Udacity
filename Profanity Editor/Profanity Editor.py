import urllib
import requests

def read_text():
	text = open(r'C:\Users\dakil\Desktop\Udacity\Profanity Editor\TestText.txt')
	contents = text.read()
	print(contents)
	text.close()
	profanity_checker(contents)

def profanity_checker(text_to_check):
	req = requests.get(r'http://www.wdylike.appspot.com/?q=' + text_to_check)
	output = req.text
	print(output)
	if req == True:
		print('There is profanity!!')
	else:
		print('There is no profanity!!')
	print(output)
	req.close()

read_text()