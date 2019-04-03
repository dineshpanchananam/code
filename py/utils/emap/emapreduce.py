# Author: Dinesh Panchananam
# Date  : 27-10-2014
# Language : Python 2.7
# About : map and reduce partial functions.
# Motto : Never write a lambda again!. 

class EMapReduce:
    @staticmethod
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
    
    @staticmethod
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
