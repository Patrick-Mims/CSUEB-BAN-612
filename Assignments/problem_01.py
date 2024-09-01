import re
import random

# use regex to search the string
def password_checker(word):
	if(re.search('[0-9]', word) and 
		re.search('[A-Z]', word) and 
		re.search('[a-z]', word)):
		# return True if the word meets standards, else False
		return True	
	return False

def random_password():
	# set the the minimum and maximum ASCII values as constants
	MIN_ASCII=33 
	MAX_ASCII=126

	# count
	i=0

	# generate the password length (including 7 and 11)
	random_int=random.randint(7,11) 

	# declare and set an empty string to accomodate the password
	generated_password="" 

	# random_int determines the number of iterations
	while(i < random_int):
		randomChar=chr(random.randint(MIN_ASCII, MAX_ASCII))
		generated_password=generated_password + randomChar
		i = i + 1

	# display the generated password
	print("Generated Password: ", generated_password)

	# result output
	print("The password generated is: ", password_checker(generated_password))

def main():
	random_password()
 
if __name__ == '__main__':
	main()
