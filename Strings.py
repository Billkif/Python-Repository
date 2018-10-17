# this section deals with strings and their manipulations

print('"Hello, world!" she said')# this one runs well because of the use of different quotes for the strings
#print('Let's go!') this wont run because of the use of the same quotes,so python will take the first two but wont know what to do with the next

print('Let\'s go!')# this will run very well since the single quotation has been emphasized upon using the backslash character

#concatenation
x = "Hello, "
y = "world!"
print(x + y)

#Long strings
print('''This is a very long string that might probably not end\n unless i decide otherwise\n
and in that case then only will it be put to an end!!''')

#rawStrings
print(r'C:\nowhere')
print(r'Let\'s go!')
print(r'C:\Program Files\foo\bar' '\\')

#Unicodes (for more visit: http://unicode-table.com)
print("\u00C6") #prints a special character i cant represent since its not on my keyboard
print("\U0001F60A")# prints a smiling emoji
print("This is a cat: \N{Cat}")# this prints out a little cute cat
