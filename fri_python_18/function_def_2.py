def sayHello():
	print('Hello')
	
def sum2(a, b):
	s = a ** b
	return s
	
import time
def test1():
	print('#test1')
	st = time.time()
	res = sum2(10000, 1000000)
	et = time.time()
	dt = et - st
	print('#time:', dt)
	
# процедура
sayHello()


# функуию 
print(sum2(10, 20))

z = sum2(1, 2)
print(z)


test1()
