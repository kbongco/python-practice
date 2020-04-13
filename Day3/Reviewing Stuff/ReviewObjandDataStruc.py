#This is from the Objects and Data Structures Assessment From the Complete Python BootCamp on Udemy 

#Strings given the string hello give an index command that returns 'e'

s = 'hello'
s[1]

#Reverse the string 'hello' using indexing
s[::-1]

#Given the string hello, give two methods of producing the letter 'o' using indexing
s[4]
s[-1]

#Build this list [0,0,0] two separate ways
list = [0,0,0]
list2 = [0]*3

#Reassign 'hello' in this nested list to say 'goodbye'

l= [1,2,[3,4,'hello']]
l[2][2] = 'goodbye'

#Sort the list below

l = [5,3,4,6,1]
sorted(l)

#Using Keys and indexing, grab the 'hello' from the 
#dictionaries

d = {'simple_key': 'hello'}
d['simple_key']

d = {'k1':{'k2':'hello'}}
d['k1']['k2']

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d['k1'][0]['nest_key'][1][0]

#Use a set to find the unique values of the list below
l = [1,2,2,33,4,4,11,22,3,3,2]
set(l)

#Booleans

2 > 3 #False
3 <= 2 #False
3 == 2.0 #False
3.0 == 3 #True
4 ** 0.5 != 2 #False