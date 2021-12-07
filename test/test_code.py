import unittest
from unittest import TestCase
from scripts import get_all_paths as paths
from scripts import list_libs as l
import os
from scripts import analyzing_my_repo as a

DIR = './test/examples'
DIR2 = './test/my_example'

class AnalyzingReposTest(TestCase):  

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

    def test_my_project(self):
        res1,res2,res3,res4 = a.analyzing_libraries(dir1='./test/returns/my_project/libs.json' , dir2='./test/returns/all_projects/libs.json', 
            dir3='./test/returns/my_project/libs_Py.json', dir4='./test/returns/all_projects/libs_Py.json')
        expected1={'os', 're', 'math'}
        expected2={'sys'}
        expected3={'Requests', 'beautifulsoup4', 'Flask'}
        expected4={'jasmine'}
        self.assertEqual(expected1,res1)
        self.assertEqual(expected2,res2) 
        self.assertEqual(expected3,res3)
        self.assertEqual(expected4,res4) 


if __name__ =="__main__":
    unittest.main()
