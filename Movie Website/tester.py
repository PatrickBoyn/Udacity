import media.py

m = media.Movie("Toy Story","A story of what toys do when you're not around.", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
print(m.title)
print(m.storyline)

try:
	print(dir(m))

except Exception as e:
	print(e)
