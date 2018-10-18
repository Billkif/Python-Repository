#this section seeks to explain the verious methods used in accessing dictionaries
#clear
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

#copy
x = {'username': 'admin','machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print(y)
print(x)

#using deepcopy
from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print(c)
print(dc)