#Question 2

def do_twice(f,s):
	f(s)
	f(s)

def print_spam():
	print('spam')

def print_twice(bruce):
	print(bruce)
	print(bruce)

def do_four(f,s):
	f(s)
	f(s)
	f(s)
	f(s)

do_four(print_twice,'spam')

do_twice(print_twice,'spam')

