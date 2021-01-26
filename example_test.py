from example import *

def test_add():
   assert add(1, 2) == 3
   assert add('Boston', 'University') == 'BostonUniversity'
   assert numpy_add(1, 2) == 3
  
def test_subtract():
   assert subtract(1, 2) == -1
   assert numpy_sub(1, 2) == - 1
