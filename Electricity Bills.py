a=str.upper('""Electricity Bill Processing""')
print(a.center(40))
print('enter your name:')
b=input()
print('Enter the consumer Number:')
c=input()
print('Enter your Home readings or Commercial Readings:')
d=input()
if d=='home':
    print(b)
    print(c)
    print('Enter the Old unit:')
    oldunit=int(input())
    print('Enter the New unit:')
    Newunit=int(input())
    paymentunit=int(Newunit-oldunit)
    print(str.upper('bill pay unit for:'),paymentunit)
    if paymentunit<=100:
        print(str.upper('No payment for you'))
    elif paymentunit<=200:
        print(str.upper('Bill payment amount:'),((paymentunit-100)*1.5)+20)
    elif paymentunit<=500:
        print(str.upper('Bill payment amount:'),((paymentunit-100)*2)+20)
    else:
        print(str.upper('Bill payment amount'),((paymentunit-100)*3)+20)

else:
    print(b)
    print(c)
    print('enter the old unit:')
    oldunit=int(input())
    print('Enter the new unit:')
    newunit=int(input())
    paymentunit=int(newunit-oldunit)
    print(str.upper('Bill pay unit for:'),paymentunit)
    print(str.upper('Bill payment amount:'),((paymentunit-100)*5)+20)





    