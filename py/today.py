Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
<turtle.Turtle object at 0x045D4450>

================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
<turtle.Turtle object at 0x03A54490>
Traceback (most recent call last):
  File "C:/Users/linda/Desktop/mypolygon.py", line 5, in <module>
    bob.fd(100)
  File "C:\Users\linda\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1637, in forward
    self._go(distance)
  File "C:\Users\linda\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1605, in _go
    self._goto(ende)
  File "C:\Users\linda\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 3158, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Users\linda\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 755, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Users\linda\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 2466, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
<turtle.Turtle object at 0x00C83B50>
Traceback (most recent call last):
  File "C:/Users/linda/Desktop/mypolygon.py", line 5, in <module>
    bob.fd(100)
  File "C:\Users\linda\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1637, in forward
    self._go(distance)
  File "C:\Users\linda\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1605, in _go
    self._goto(ende)
  File "C:\Users\linda\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 3158, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Users\linda\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 755, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Users\linda\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 2466, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
<turtle.Turtle object at 0x03911D50>
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
<turtle.Turtle object at 0x03F61A10>
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
<turtle.Turtle object at 0x03901AF0>
hello!
hello!
hello!
hello!
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
<turtle.Turtle object at 0x03BA1B30>
hello!
hello!
hello!
hello!
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
<turtle.Turtle object at 0x038D44B0>
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
<turtle.Turtle object at 0x03CF4430>
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
<turtle.Turtle object at 0x042844B0>
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
>>> if x < 0:
	pass    #TODO: need to handle negative values!
x+2
SyntaxError: invalid syntax
>>> 2+2
4
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
>>> countdown(3)
3
2
1
blastoff
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
>>> x(2)
x is positive
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
>>> x(3)
x is odd
>>> x(4)
x is even
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
>>> x(3)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x(3)
  File "C:/Users/linda/Desktop/mypolygon.py", line 21, in x
    if x < y:
NameError: name 'y' is not defined
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
>>> x(3)
>>> y(4)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    y(4)
NameError: name 'y' is not defined
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
>>> x(3)
>>> y(4)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    y(4)
NameError: name 'y' is not defined
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
>>> x(3)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x(3)
TypeError: x() missing 1 required positional argument: 'y'
>>> x(3, 4)
x is less than y
>>> x(3, 3)
x and y are equal
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
>>> choice(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    choice(b)
NameError: name 'b' is not defined
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
>>> choice(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    choice(b)
NameError: name 'b' is not defined
>>> draw(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    draw(b)
NameError: name 'draw' is not defined
>>> draw_a()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    draw_a()
NameError: name 'draw_a' is not defined
>>> import turtle
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
Traceback (most recent call last):
  File "C:/Users/linda/Desktop/mypolygon.py", line 3, in <module>
    pring(bob)
NameError: name 'pring' is not defined
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
<turtle.Turtle object at 0x036D4490>
Traceback (most recent call last):
  File "C:/Users/linda/Desktop/mypolygon.py", line 6, in <module>
    bob.fd(100)
  File "C:\Users\linda\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1637, in forward
    self._go(distance)
  File "C:\Users\linda\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1605, in _go
    self._goto(ende)
  File "C:\Users\linda\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 3158, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Users\linda\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 755, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Users\linda\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 2466, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
<turtle.Turtle object at 0x03FD1DD0>
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
<turtle.Turtle object at 0x03CA44B0>
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
<turtle.Turtle object at 0x046144D0>
Traceback (most recent call last):
  File "C:/Users/linda/Desktop/mypolygon.py", line 15, in <module>
    square(bob)
TypeError: square() missing 1 required positional argument: 'length'
>>> 
================ RESTART: C:/Users/linda/Desktop/mypolygon.py ================
<turtle.Turtle object at 0x04244490>
Traceback (most recent call last):
  File "C:/Users/linda/Desktop/mypolygon.py", line 16, in <module>
    square(bob)
TypeError: square() missing 1 required positional argument: 'length'
>>> 
