import numpy as np

'''
================================
Defining my own functions here
================================
'''

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def numpy_add(a, b):
  return np.add(a, b)

def numpy_sub(a, b):
  return np.subtract(a, b)

'''
=====================================
Defining my own testing fuctions here
=====================================
'''
def test_add():
  assert add(1, 2) == 3
  assert add('Boston', 'University') == 'BostonUniversity'
  assert numpy_add(1, 2) == 3
  
def test_subtract():
  assert subtract(1, 2) == -1
  assert numpy_sub(1, 2) == - 1
 
 


