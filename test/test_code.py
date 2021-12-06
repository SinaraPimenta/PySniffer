import unittest
from unittest import TestCase
import sys, os
from scripts import get_all_paths as paths
from scripts import list_libs as l

DIR = './test/examples'

class AnalyzingReposTest(TestCase):  

    #@classmethod
    #def setUpClass(self): 
        
        #os.system(f'python pipreqs/pipreqs.py {DIR}/repo1 --force')    
        #os.system(f'python pipreqs/pipreqs.py {DIR}/repo2 --force')   
        #os.system(f'python pipreqs/pipreqs.py {DIR}/repo3 --force') 
        # 
    def setUp(self):
        l.arr_py = []
        l.arr = []

    def test_get_projects(self):
        expected = {'repo1': 3, 'repo2': 3, 'repo3': 2}
        response = paths.get_projects(DIR)
        self.assertEqual(expected,response)

    def test_count_files(self):
        expected = 8
        response = paths.count_files(DIR)
        self.assertEqual(expected,response)

    def test_read_files(self):
        l.read_requirements(DIR +'/repo1')
        expected_py = ['math', 'datetime', 're', 'calendar']
        expected_ext = ['Flask', 'numpy', 'pygame', 'pytest']
        self.assertEqual(expected_py,l.arr_py)
        self.assertEqual(expected_ext,l.arr)

    def test_count_libs(self):
        l.read_requirements(DIR +'/repo1')
        myDictReturn,myDictPyReturn = l.count_libs()
        expected_ext = [{'name': 'Flask', 'amount': '1'}, {'name': 'numpy', 'amount': '1'}, {'name': 'pygame', 'amount': '1'}, {'name': 'pytest', 'amount': '1'}]      
        expected_py = [{'name': 'math', 'amount': '1'}, {'name': 'datetime', 'amount': '1'}, {'name': 're', 'amount': '1'}, {'name': 'calendar', 'amount': '1'}]  
        self.assertEqual(expected_py,myDictPyReturn)
        self.assertEqual(expected_ext,myDictReturn) 

if __name__ =="__main__":
    unittest.main()
