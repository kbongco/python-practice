#From the Complete Python Bootcamp from Udemy 

#Use for, split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'

for words in st.split():
    if words[0] == 's':
        print(words)

#Use Range to print all even numbers from 0 to 10
for x in range(0,11,2):
    print(x)

#Use list comprehension to create a list of all numbers
# between 1 and 50 that are divisible by 3 

div_by_three = [print(x) for x in range(1,51) if x % 3 == 0]  

#Go through the string below and if the length 
#of a word is even print even! 

st1 = st1 = 'Print every word in this sentence that has an even number of letters'

for word in st1.split():
    if len(word) % 2 == 0:
        print(word)

#Use list comprehension to create a list
#of the first letters of every word in the string below

st2 = 'Create a list of the first letters of every word in this string'
list2 = [print(word[0]) for word in st2.split()]