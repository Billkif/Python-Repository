#this section explains the process of string formatting
format = "Hello, %s. %s enough for ya?"
values = ('world', 'Hot')
print(format % values)

#Using string template
from string import Template
tmpl = Template("Hello, $who! $what enough for ya?")
print(tmpl.substitute(who="Mars", what="Dusty"))

#bracket formating
print("{}, {} and {}".format("first", "second", "third"))
print("{} {} {} {} {} {}".format("be", "not","or","to"))

#including float formating
from math import pi
print("{name} is approximately {value:.2f}.".format(value=pi, name="pi"))

from math import e
print(f"Euler's constant is roughly {e}.")  
