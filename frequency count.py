#This program says hello and asks for my name
print('What is your name?')
myName=str.lower(input())
print('It is good to meet you',myName)
print('The length of your Name is:')
print(len(myName))
print('What is your age?') #ask for their age
myAge=int(input())
if myAge>=18:
    print('your the elder')
else:
    print('your the younger')
print('a -',myName.count('a'),',b -',myName.count('b'),',c -',myName.count('c'),',d -',myName.count('d'),',e -',myName.count('e'),',f -',myName.count('f'))
print('g -',myName.count('g'),',h -',myName.count('h'),',i -',myName.count('i'),',j -',myName.count('j'),',k -',myName.count('k'))
print('l -',myName.count('l'),',m -',myName.count('m'),',n -',myName.count('n'),',o -',myName.count('o'),',p -',myName.count('p'))
print('q -',myName.count('q'),',r -',myName.count('r'),',s -',myName.count('s'),',t -',myName.count('t'),',u -',myName.count('u'))
print('v -',myName.count('v'),',w -',myName.count('w'),',x -',myName.count('x'),',y -',myName.count('y'),',z -',myName.count('z'))