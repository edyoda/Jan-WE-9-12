# import pdb
def linear_search(l,key):
	for value in l:
		if key == value :
			return True
	else:
		return False	

# pdb.set_trace()
l = [10,20,30,40,50,60]
key = 40 

result = linear_search(l,key)
print(result)