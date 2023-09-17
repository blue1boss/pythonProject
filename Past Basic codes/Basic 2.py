'''
A list is a collection of items in a particular order.
In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas(,).
A few list examples are listed below:

['cat', 'bat', 'rat', 'elephant']
'''

#save a list in a variable named "letters"
letters = ['a', 'b', 'c', 'd']
print(letters) #print the list
type(letters) #check the type of object in the "letters" variable: call the `type()` function.

list = [1,"book",True,[3,4]]
len(list)
print(len(list))
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
# check the length of the list `spam`
print(len(spam))

#print your name
names=['Jenny',"Jim"]
print(names)

#Index Positions Start at 0, Not 1.
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)
print(spam[0]) # access the 1st element (index = 0) in the list.

print(len(spam))
# what will happen if can use an index that exceeds the number of values in the list?
spam[2]

#Given the following list, please print the 2nd and the last element in the list respectively.
colors = ['red', 'green', 'blue', 'yellow']
# print the 2nd element:
print(colors[1]) #green
# print the last element:
print(colors[-1]) #yellow

colors=['9','10','11']
print(colors[1]) #10
print(colors[-1]) #11

'''
List values have an index() method that can be passed a value, and if that value exists in the list, the index of the value is returned. 
If the value isn’t in the list, then Python produces a ValueError error.
'''

names = ['hello', 'hi', 'howdy', 'heyas','Zophie', 'Pooka', 'Fat-tail', 'Pooka','Alice', 'Bob']
names.index('hello') #0

#find index
names = ['hello', 'hi', 'howdy', 'heyas','Zophie', 'Pooka', 'Fat-tail','Alice','Bob','badgers', 'ants']
#write code below:
names.index('Bob')

'''
Changing, Adding, and Removing Elements
Most lists you create will be dynamic, meaning you’ll build a list and then add and
remove elements from it as your program runs its course.
'''

colors = ['red', 'green', 'blue', 'yellow']
print(colors)
# change the value of the first element to 'black'
colors[0]='black'
print(colors)

#['red', 'green', 'blue', 'yellow']
#['black', 'green', 'blue', 'yellow']


'''
Adding element 
'''

colors = ['red', 'green', 'blue', 'yellow']
print(colors)

#1st way: append the item to the end of the list. append() is a function for the list data type.
colors.append("white")
print(colors)
# insert the color "orange", and print the list.
colors.append('orange')
print(colors)

#2nd way: insert the element at any position: insert() is a function for element insertion at specific location.
# Syntax: insert(position_index, item_value)
colors.insert(0,"purple")
print(colors)
# insert the color "black" as the first element, and print the list.
colors.insert(0,'black')
#print the number of elements in the list.
print(colors)
print(len(colors)) #len() function: check the # of items

'''
#removing : use the
# del statement, pop(index) (default: -1) or remove(value).
'''
colors = ['red', 'green', 'blue', 'yellow','black']
print(type(colors)) # print the type
print(len(colors)) # print the # of elements
print(colors) # print the elements

#remove the last element
colors.pop(-1)
print(colors)

#remove the first element using pop()
colors.pop(0)
print(colors)

#remove the first element
del colors[0]
print(colors)

#remove the last element using del
del colors[-1]
print(colors)

# remove 'yellow` from the list using remove(), and print the list.
colors.remove('blue')
print(colors)

'''
List Slicing
To make a slice, you specify the index of the first and last elements you want to work with.
'''
players = ['charles', 'martina', 'michael', 'florence', 'eli', 'Sonia']
print(players[2:4]) #including index=2, but excluding index=4
print(players[:2]) # the same as print(players[0:2])
print(players[-5:-2])

# can you guess the output of the code below: 
print(players[-3:])
# print the first two elements in the list:
print(players[0:2])
# print hte last two elements in the list:
print(players[-2:])