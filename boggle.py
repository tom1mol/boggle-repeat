from string import ascii_uppercase
from random import choice       #choice function returns an item from a list at random



def make_grid(width, height):
    
    #create grid that will hold all of the tiles for a boggle game
    #function creates a dictionary with row/column tuple as the key..and a space as the value
    return {(row, col): choice(ascii_uppercase)
        for row in range(height)
        for col in range(width)
}


def neighbours_of_position(coords):
    
    #get neighbours of a given position
    
    row = coords[0]
    col = coords[1]
                                                                    # (-1,-1)  (-1,0)  (-1,1)
                                                                    # (0, -1)  (0,0)   (0,1)
                                                                    # (1,-1)  (1,0)   (1,1)
    #assign each of the neighbours
    #top left to top right
    top_left = (row - 1, col - 1)
    top_center = (row -1, col)
    top_right = (row - 1, col +1)
    
    #left to right
    left = (row, col - 1)
    #the (row, col) coordinates passed to this function are situated here
    right = (row, col + 1)
    
    #bottom-left to bottom-right
    bottom_left = (row + 1, col - 1)
    bottom_center = (row + 1, col)
    bottom_right = (row + 1, col + 1)
    
    return [top_left, top_center, top_right,
            left, right,
            bottom_left, bottom_center, bottom_right]
    
def all_grid_neighbours(grid):
    #get all possible neighbours for each position in the grid
    
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
        
    return neighbours
    
        