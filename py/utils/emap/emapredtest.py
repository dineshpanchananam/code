from emapreduce import EMapReduce
def test_samples():
	emap = EMapReduce.emap
	ereduce = EMapReduce.ereduce
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
