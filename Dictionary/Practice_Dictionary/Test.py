# from random import *

# def Guss(x):
# 	R = randint(1,x)
# 	g = 0
# 	while g is not R:
# 		g  = int(input("Enter: "))
# 		if(g<R):
# 			print("Too low")
# 		elif(g>R):
# 			print("Too high")
# 	print("Yes congrats")
# Guss(10)
# import heapq
# my_dict = {'x':500, 'y':5874, 'z': 560}
# # t =max((['x', 'y', 'z']),key=(lambda k:my_dict[k]))
# # print(t)
# t = heapq.nlargest(1,my_dict)
# print(t)
import collections as c
help(c.Counter)