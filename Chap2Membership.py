#this section uses the boolean operator 'in' to check whether 
#a particular element is found in the sequence

permissions = 'rw'
print('w' in permissions)#prints True
print('x' in permissions)#prints False
#another list

users = ['mlh','foo','bar']
promt = input('Enter your user name: ')
print(promt in users)
subject = '$$$ Get rich now!!! $$$'
print('$$$'in subject)
