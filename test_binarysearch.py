from binsearch import binary_search

import unittest
import numpy as np

class MyTest(unittest.TestCase):
    
    def setUp(self):
        self.inputt = range(10)
        
    def tearDown(self):
        del self.inputt
    
    #test showing that sorted array is necessary- 3 is present but returns -1
    def test_sorted(self):
        self.assertEqual(binary_search([2,1,5,3,6],3),-1)
    
    #test for searching in an empty array
    def test_empty(self):
        self.assertEqual(binary_search([],2), -1)   
    
    #test for searching in an array with 1 element when object present   
    def test_1el_pres(self):
        self.assertEqual(binary_search([1],1), 0)  
    
    #test for searching in an array with 1 element when object not present       
    def test_1el_npres(self):
        self.assertEqual(binary_search([1],2), -1)       
    
    #test for search in 2 element array when object present    
    def test_2el_pres(self):
        self.assertEqual(binary_search([1,2],1), 0)  
    
    #test for search in 2 element array when object not present 
    def test_2el_npres(self):
        self.assertEqual(binary_search([1,2],3), -1)      
        
    #test for passing in non-array 
    def test_not_array(self):
        with self.assertRaises(TypeError):
            binary_search(1,2)     
            
    #test for passing in strings
    def test_non_numeric_str(self):
        with self.assertRaises(TypeError):
            binary_search(['l','ol'],2)  
            
    def test_chr(self):
        self.assertEqual(binary_search(['a','b','c','d'],'c'),2)         
    
    #test for whether NaN is valid input in array      
    def test_non_numeric_nan(self):
        self.assertEqual(binary_search([1,2,float('NaN'),float('NaN')],2),1)
    
    #test for whether inf is valid input in array         
    def test_non_numeric_inf(self):
        self.assertEqual(binary_search([1,2,np.inf],np.inf),2) 
     
    #test for normal search in array 
    def test_easy_case(self):
        self.assertEqual(binary_search(self.inputt,2), 2)
    
    #test for a needle in between values in array
    def test_in_btw(self):
        self.assertEqual(binary_search(self.inputt,4.5), -1)
    
    #test for needle outside of the bounds of array (to the right)    
    def test_off_right(self):
        self.assertEqual(binary_search(self.inputt,11), -1)  
    
    #test for needle outside of the bounds of array (to the left)        
    def test_off_left(self):
        self.assertEqual(binary_search(self.inputt,-2), -1)    
    
    #test for showing multiple needle behavior  
    def test_multiple_answers(self):
        self.assertEqual(binary_search([1,1,2,2,3,3,4],3),5) #finds the second 3 
        self.assertEqual(binary_search([0,1,1,2,2,3,3,4],3),5) #finds the first 3
    
    #test for needles on left end of array
    def test_extreme_needlel(self):
        self.assertEqual(binary_search(self.inputt,0), 0) 
    
    #test for needles on right end of array    
    def test_extreme_needler(self):
        self.assertEqual(binary_search(self.inputt,9), 9)
    
    #test for behavior when left and right dont include needle in between   
    def test_set_index_npres(self):
        self.assertEqual(binary_search(self.inputt,5,1,3), -1) 
    
    #test for behavior when left and right do include needle in between 
    def test_set_index_pres(self):
        self.assertEqual(binary_search(self.inputt,2,1,3), 2)       

    #test shows that left value must be <= right value in order for search to work
    def test_rev_index(self):
        self.assertEqual(binary_search(self.inputt,2,3,1), -1) 
    
    #test for behavior when left and right start out equal when element present    
    def test_same_index_pres(self):
        self.assertEqual(binary_search(self.inputt,2,2,2), 2) 
    
    #test for behavior when left and right start out equal when element not present    
    def test_same_index_npres(self):
        self.assertEqual(binary_search(self.inputt,5,2,2), -1)  
         
    
