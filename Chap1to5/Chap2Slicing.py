#this section explains slicing as a form of indexing to access a range of elements

 tag = '<a href="http://www.python.org">Python web site</a>'
 print('domain name: ' + tag[9:30])
 print('title of site: ' + tag[32:-4]
 
 #when supplying two indices, you are setting limits, the first being inclusive and the other exclusive

 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 print(numbers[3:6])
 print(numbers[0:1])
 #a nifty shortcut, explicit indexing
 print(numbers[7:10])
 #indexing from the right
 print(numbers[-3:-1])
 #leaving out an index,permits you to print the rest of the sequence from
 #the index used to the end,same from the right
 print(numbers[-3:])#prints 8,9,10
 print(numbers[:3])#prints 1,2,3
 #for the entire sequence
 print(numbers[:])
 #longer steps for slicing
 print(numbers[0:10:1])#prints the whole sequence with steps of one
 print(numbers[0:10:2])#prints the sequence with steps of two
 print(numbers[8:3:-1])#prints from left from index 8 with one step
 print(numbers[10:0:-2])#prints from left from index 10,to index 0 with step 2
 print(numbers[::-2])#shortcut for the same result above
 
