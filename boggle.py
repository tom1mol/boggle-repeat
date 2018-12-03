def make_grid(width, height):
    
    #create grid that will hold all of the tiles for a boggle game
    #function creates a dictionary with row/column tuple as the key..and a space as the value
    return {(row, col): ' ' for row in range(height)
        for col in range(width)
}
