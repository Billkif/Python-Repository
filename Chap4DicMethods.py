#this section seeks to explain the verious methods used in accessing dictionaries

d = {}
d['name'] = 'Gumby'
d['age'] = 42
print(d)
returned_value = d.clear()
print(returned_value)

#application of the clear method
x = {}
y = x
x['key'] = 'value'
print(y)
x.clear
print(y)