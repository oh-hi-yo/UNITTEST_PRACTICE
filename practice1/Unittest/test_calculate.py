import unittest  
from PRODUCT.calculate import square, suare_plus_five  
  

class ExampleTest(unittest.TestCase):  
    """Test example  
    """  
    def test_func2(self):  
        self.assertEqual(square(5), 25)  
        self.assertEqual(suare_plus_five(-5), 0) 