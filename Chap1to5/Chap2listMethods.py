#this section demonstrates some operations of list functions

#append
lst = [1, 2, 3]
print(lst)
lst.append(4)
print(lst)

#clear
lst.clear
print(lst)

#copy
a = [1, 2, 3]
b = a
b[1] = 4
print(a)#this affects the list of a aswell
#to solve this
a = [1,2,3]
b = a.copy()
b[1] = 4
print(a)#a remains unchanged since only a copy of it was assigned to b

#count
 x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
 print(x.count(1))
 print(x.count([1, 2]))

 #extend
 a = [1, 2, 3]
 b = [4, 5, 6]
 a.extend(b)
 print(a)

 #index: used for searching lists for the first occurance of a word
knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
print(knights.index('who'))

#insert; used to insert an object into a list
numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
print(numbers)

#pop; removes an element which is the last one by default, and returns it
x = [1, 2, 3]
print(x.pop())#returns 3 by default
print(x.pop(0))#returns 1
print(x)#prints only [2]

#remove; used to remove first occurance of a value
 x = ['to', 'be', 'or', 'not', 'to', 'be']
 x.remove('be')
print(x)

#reverse; reverses the elements in the list
x = [1, 2, 3]
x.reverse()
print(x)

#sort; used to sort list in right order
x = [4, 6, 2, 1, 7, 9]
x.sort()
print(x)
x = [4, 6, 2, 1, 7, 9]
y = sorted(x)#returns the list of sorted x to y
print(y)

#advanced sorting; can use two arguments in sort method; key and reverse
 x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
 x.sort(key=len)#this step assigns a key to each element in the list and in this case is their lenghts
 print(x)#from here the elements are sorted based on their lenghts
x = [4, 6, 2, 1, 7, 9]
x.sort(reverse = True)#just a boolean expression to whether the sequence be printed in reverse order
print(x)
 
