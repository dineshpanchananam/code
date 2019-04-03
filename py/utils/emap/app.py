# Author: Dinesh Panchananam
# Date  : 27-10-2014
# Language : Python 2.7
# About : map and reduce partial functions.
# Motto : Never write a lambda again!. 

def emap(query_string):
	# query_string should be 
	# of from vars separator expression  
	# separator can be => or -> or ':'
	# eg 'x => x*x', 'x -> x**2' , 'x: x*x*x'
	# or x,y => x+y, x,y -> x*y, x,y : x/y

	# since the user has a choice of separator we need to
	# find out the separator so as to split the query_string.
	sep = [sym for sym in ('=>', ':', '->') if sym in query_string][0]
	
	# split the query_string into left hand and right hand sides
	query_left, query_right = query_string.split(sep)

	# now we define a lambda 
	# which takes a mappable_iterable and 
	# maps our query_string_essence onto it.
	# which leads to a partial function and returns it

	return lambda alist: eval('map ( lambda (%s): %s , %s)'%(query_left, query_right, alist))

def ereduce(query_string):
	# query_string should be 
	# of from var(s) separator expression  
	# separator can be => or -> or ':'
	# eg 'x => x*x', 'x -> x**2' , 'x: x*x*x'
	# or x,y => x+y, x,y -> x*y, x,y : x/y

	# since the user has a choice of separator we need to
	# find out the separator so as to split the query_string.
	sep = [sym for sym in ('=>', ':', '->') if sym in query_string][0]
	
	# split the query_string into left hand and right hand sides.
	query_left, query_right = query_string.split(sep)

	# now we define a lambda 
	# which takes a mappable_iterable and 
	# applies our query_string_reduce onto it
	# which leads to a partial function and returns it.

	return lambda alist: eval('reduce ( lambda %s: %s ,%s)'%(query_left, query_right, alist))


def test_samples():
	# some emap snippets
	cube = emap('x->x**3') # code re-use
	print cube([1, 2, 4]) #[1, 8, 64]
	print emap('x:x*x')([1, 2, 4])  # anonymous if you like, warning: one time use only
	print emap('x,y:x+y')([[1, 2], [3, 4]]) #[6, 7]
	
	#some ereduce snippets
	mult = ereduce('x,y->x*y') # code reuse
	print mult([1, 2, 3]) # 6
	print ereduce('x,y=>x+y')([1, 2, 4]) #6


	# map and reduce
	# sum of squares of each of [1, 2, 4]
	# so simple.

	print ereduce('x,y=>x+y')(emap('x:x*x')([1, 2, 4]))  #21
	# over.

def main():
	# run a sample 
	test_samples()

if __name__ == '__main__':
	main()
