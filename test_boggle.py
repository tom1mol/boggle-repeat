import unittest     #unittest framework uses classes and inherritance
                    #we create a class that inherits from the testcase class in the framework and write
                    #methods inside that class for the actual tests
                    
import boggle   #this is where code we are testing resides(boggle.py)

class TestBoggle(unittest.TestCase):    #create class inheriting from test case and add docstring to explain purpose
    #test suite for boggle solver
                                        #test method with docstring giving shot description
    def test_can_create_an_empty_grid(self): #this case empty grid no assumptions 4 grid shape or data structure used
        #test to see if we can create an empty grid
        grid = boggle.make_grid(0, 0) #height & width or row and column. (0,0) = no rows or columns
        self.assertEqual(len(grid), 0) #0 x 0 grid has a length of 0
        
    def test_grid_size_is_width_times_height(self):
        #test to ensure total size of grid is w x h
        
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)
        
        
    def test_grid_coordinates(self):
        
        #test to ensure that all the coordinates of the grid can be accessed
        
        grid = boggle.make_grid(2, 2)
        self.assertIn((0, 0), grid) #use assertIn method to check is (0,0) in a 2x2 grid
        self.assertIn((0, 1), grid)
        self.assertIn((1, 0), grid)
        self.assertIn((1, 1), grid)
        self.assertNotIn((2, 2), grid)
        