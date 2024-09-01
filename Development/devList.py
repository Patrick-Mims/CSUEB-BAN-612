from collections import deque

def show_movie():
	print("Coming to America")

	movies = [ "Only in America.", "America the Beautiful.", "Born in the USA." ]
	movies.append("Enemy of the State.")
	movies.append("War Games.")

	# for
	print("[ For ]")
	for movie in movies:
		print(movie)

	print()

	# List Comprehension
	print("[ List Comprehension ]")
	[ 
		print("Watched -> " + movie) for movie in movies 
	]

	print()

	# range 
	print("[ Range ]")
	for i in range(len(movies)):
		print("The list at index", i, " -> ", movies[i])

	print()

	# enumerate
	print("[ Enumerate ]")
	for index, element in enumerate(movies):
		print(index, element)

	print()

	# [ while ]
	i = 0	
	while i < len(movies):
		print("==> ", movies[i])
		i = i + 1

	print("movies.reverse() ", movies.reverse())

	print("movies.reverse() ", movies.reverse())

show_movie()

def create_stack():
	print("YouTube")

create_stack()

def create_dictionary():
	print("create dictionary...")
	

def create_stack():
	print("Creating a Stack...")

create_dictionary()
create_stack()

