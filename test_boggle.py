import unittest     #unittest framework uses classes and inherritance
                    #we create a class that inherits from the testcase class in the framework and write
                    #methods inside that class for the actual tests
                    
import boggle   #this is where code we are testing resides(boggle.py)
from string import ascii_uppercase

class TestBoggle(unittest.TestCase):    #create class inheriting from test case and add docstring to explain purpose
    #test suite for boggle solver
                                        #test method with docstring giving short description
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
        
        
    def test_grid_is_filled_with_letters(self):
        
        #ensure each of the coordinates in the grid contains letters
        
        grid = boggle.make_grid(2, 3)
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)
            
            
    
    def test_neighbours_of_a_position(self):
        
        #ensure that a position has 8 neighbours. function takes a position and returns 8 neighbours it should have
        
        coords = (1, 2)
        neighbours = boggle.neighbours_of_position(coords)
        self.assertIn((0, 1), neighbours)
        self.assertIn((0, 2), neighbours)
        self.assertIn((0, 3), neighbours)
        self.assertIn((1, 1), neighbours)
        self.assertIn((1, 3), neighbours)
        self.assertIn((2, 1), neighbours)
        self.assertIn((2, 2), neighbours)
        self.assertIn((2, 3), neighbours)
        
    def test_all_grid_neighbours(self):
        #ensure all grid positions have neighbours
        
        grid = boggle.make_grid(2, 2)
        neighbours = boggle.all_grid_neighbours(grid) #get all neighbours 4 grid.
                                 #is a dictionary where key is position and value is list of neighbouring positions
        self.assertEqual(len(neighbours), len(grid)) #assert correct length of neighbours dictionary
        for pos in grid:      #for loop iterates through positions in grid. for each pos neigh are other 3 positions
            others = list(grid) #creates new list from the dictionaries keys. this is full list
            others.remove(pos) #minus position in question
            self.assertListEqual(sorted(neighbours[pos]), sorted(others)) #asserts pos neigh are pos being checked
            
        
        
        
        