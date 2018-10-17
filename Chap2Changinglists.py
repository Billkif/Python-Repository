#this section shows how items in list can be replaced
#replacing elements
x = [1, 1, 1]
print(x)
x[1] = 2
print(x)

#deleting elements
 names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
 del names[2]
 print(names)

 #assigning to slices
 name = list('Perl')
 print(name)
 name[2:] = list('ar')
 print(name)

 numbers = [1,5]
 print(numbers)
 numbers[1:1] = [2,3,4]
 print(numbers)