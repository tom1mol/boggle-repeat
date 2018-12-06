
#import os                                                  #from challenge solution
from string import ascii_uppercase
from random import choice       #choice function returns an item from a list at random

#SCRIPT_PATH = os.path.join(os.getcwd(), os.path.dirname(__file__))     #from challenge solution


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
    
        
def path_to_word(grid, path):
    #add all of the letters on a path to a string
    #gets list of letters for positions in a path and then jois them into a string
    return ''.join([grid[p] for p in path])
    


    
    
def search(grid, dictionary): #function that accepts a grid and a dictionary
    #search through the paths to locate words by matching strings to words in a dictionary
    
    neighbours = all_grid_neighbours(grid) # 1st get neighbours of every position in grid
    paths = []  
    full_words, stems = dictionary 
    
                #unpsack dictionary tupple into stems and full_words
                #then get path list to capture all paths that form valid words
                #store words as paths because it allows us identify each individual letter
                #search function starts a search by passing a single position to do_search(1 letter)
                #do search converts whatever path thatsgiven into a word and checks if its in the dictionary
                #if path makes a word its added to the paths list. whether path is word or not, do search gets each
                #of the neighbours of the last letter to make sure the neighbouring letter isnt already in the path
                #and continues the searching from that letter. do_seasrch can call itel 8 times for each starting 
                #position and again for each of the various neighbours of each neighbour. for each position in the grid
                #we do a search and convert all the paths and make valid words into words and return them in a list
                
    def do_search(path): #nested inside search function. cant be called directly. has access to variables withing
        word = path_to_word(grid, path) #search function(paths) which it can add to
        if word in full_words:      #do_search can be called by search function and can call itself
            paths.append(path)
        if word not in stems:
            return
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
                
    for position in grid:
            do_search([position])
            
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)
    
def get_dictionary(dictionary_file):
    #load dictionary file
    
    full_words, stems = set(), set()    #tuple,2 sets. 1 set with full words, other set with stems
    
    with open(dictionary_file) as f:
        for word in f:
            word = word.strip().upper()
            full_words.add(word)
            
            for i in range(1, len(word)):
                stems.add(word[:i])
                
    return full_words, stems
    
    # if not dictionary_file.startswith('/'):                               #from challenge solution
    #     # if not absolute, then make path relative to our location:
    #     dictionary_file = os.path.join(SCRIPT_PATH, dictionary_file)

    
        
        
def display_words(words):
    for word in words:
        print(word)
    print("Found %s words" % len(words))
    
    
def main():
    #this is the function that will run the whole project
    
    grid = make_grid(3, 3)  #generate random board
    dictionary = get_dictionary('words.txt')    #load a dictionary
    words = search(grid, dictionary)    #find the words
    # for word in words:                                
    #     print(word) #print them out               this was moved to def display_words(words)
    # print("Found %s words" % len(words))
    display_words(words)
    
#main()    ..when we run unittest it runs the tests and the solver with main() command
        #creates grid of letters, loads dictionary and prints a list of words
        #this is a problem where running the tests..boggle.py gets imported and executed 
        #to avoid running code when the file is imported...we use the following if statement
    
   
if __name__ == "__main__":
    
    #code in here will only run when file is run directly
    main()
    
    
    
    
    