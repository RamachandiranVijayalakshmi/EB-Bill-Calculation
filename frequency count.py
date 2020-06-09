def my(myName,myAge):
    print('It is good to meet you',myName)
    print('The length of your Name is:',len(myName))
    countlist=dict()
    for char in myName:
       count=myName.count(char)
       countlist[char]=count
    print(countlist)
a=str.lower(input('What is your name?'))
b=int(input('What is your age?'))
my(a,b)
