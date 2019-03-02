import threading
import time

def sqr(num):
	global count
	print("Inside sqr function")
	lock.acquire()
	lock.acquire()
	for value in range(5):
		count+=10
		print(count)
		time.sleep(2)
	lock.release()
	lock.release()

def multiply(num1,num2):
	global count
	print("Inside multiply function")
	# lock.release()
	lock.acquire()
	for value in range(5):
		count+=2
		print(count)
		time.sleep(1)
	lock.release()


count = 100
lock = threading.RLock()
t1 = threading.Thread(target= sqr, args=(5,))
t2 = threading.Thread(target = multiply, args= (5,6))

t1.start()
t2.start()

# race condition 
# deadlock 
