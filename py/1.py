import math 

def run(f):
  f()
  return f


@run
def demo1():
  assert 1 == 1
  
@run  
def demo2():
  assert 55==55

@run 
def demo3(): 
 r = 5
 assert 523.599==round(4/3 * math.pi * r ** 3,3)
  
  