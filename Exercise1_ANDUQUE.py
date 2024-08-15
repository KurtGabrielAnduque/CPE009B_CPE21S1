#NUMBERS
varNum = 123
pi = 3.14159

#STRINGS
varString = "Hello World!"
varText = 'This is a String'

#LISTS
varList = ["abc", 123]

#TUPLES
varTuple = 'abc',123,"HELLO"


#DICTIONARIES
var = 3
varDict = {'first':1,'2':'2nd',3:var}

varDict = {}
varDict['first'] = 1
varDict['2'] = '2nd'
varDict[3] = var

#Arithmetic operations
a = 5 + 3
print(a)
# >8

b = 5 - 3
print(b)
# >2


c = 5*3
print(c)
# >15

d = 5 ** 3
print(d)
# >125

e = 5/3
print(float(e))
# >1.6666666666666667

f = 5%3
print(f)
# >2

g = 5//3
print(g)
# >1


#Increment/Decrement
a = 5
a += 1
print(a)
# >6


#Decrement
a = 5
a -= 1
print(a)
# >4


a = 'Hello' + 'World'
print(a)
# >Hello World!


#Complex Expression
a = 3 + 5 - 6 * 2 / 4
print(a)
# >5.0

print('\n')
#Boolean Conditions
x = True

if x:
    print("var x is True")
else: 
    print("var x is False")
# > var x is True
    

#String conditions
x = 'Hello World!'

if x == 'Hello World!':
    print('var x is Hello World!')
else: 
    print('var x is not Hello World!')
# var x is Hello World!


#Numerical Conditions
x = int(10)

if x == '10':
    print('var x  is a string')
elif x == 10:
    print("var x is an integer")
else:
    print("var x is none of the above")
# var x is an integer


#For Loops
for var in range(0,5,2):
    print(var)

#While Loops
var = 0
while var < 5:
    print(var)
    var += 2
    
#Nested Loops
x = 0
while x < 5:
    for y in range (0,x):
        print(y, end=' ')
    x += 1
    print()
    
print('\n')

#LISTS
pi = 3.14159
varList = [1,2,'A','B','Hello!',pi]
print(varList[0])

print(varList[4])

varList.append('World!')
print(varList[6])

len(varList)
print(len(varList))

print(varList[5])

varList.remove(pi)
print(varList[5])


#DICTIONARIES
print('\n')
var = "Hello World!"
varDict = {'first':123, 2:'abc', '3': var, 4:['lista','listb']}
print(varDict['first'])
print(varDict[2])
print(varDict['3'])
print(varDict[4])
print(varDict[4][1])
print(len(varDict))

print('\n')

#LIST GENERATIRS AND COMPREHENSION
def gen_num_up_to(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(gen_num_up_to(5))

varList = gen_num_up_to(5)
print([var for var in varList])

def gen_num_up_to (n):
    num = 0
    while num < n:
        yield num
        num += 2
    
varList = gen_num_up_to(5)
print([var for var in varList])

varList = range(0, 5, 2)
print([var for var in varList])


#Slicing
print('\n')
varList = [1,2,3,4,5,6,7,8,9,10]
print(varList[:5])
print(varList[5:])
print(varList[:-2])
print(varList[-2:])
print(varList[2:-2])
print(varList[2:8:2])

print('\n')

#FUNCTIONS

def remainder(n,m):
    while True:
        if n - m < 0:
            return n
        else:
            n = n - m
            

print(remainder(10,4))


