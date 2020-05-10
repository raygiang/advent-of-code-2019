import math
from itertools import permutations

class Robot:
    def __init__( self, instruction_list ) :
        self.instructions = instruction_list
        self.i = 0
        self.relative_pos = 0
        self.x = 0
        self.y = 0
        self.direction = 0
        self.painted_tiles = dict()
        self.painted_tiles[( 0, 0 )] = 1
        self.output = []
        
    def run_diagnostic( self ) :
        while self.i < len( self.instructions ) :
            operation = self.instructions[self.i]
    
            if operation == 99:
                break
    
            mode_one = math.floor( operation % 1000 / 100 )
            mode_two = math.floor( operation % 10000 / 1000 )
            mode_three = math.floor( operation % 100000 / 10000 )
    
            if operation % 100 != 3 and operation % 100 != 4 :
                if mode_one == 2 :
                    try : number_one = self.instructions[ self.relative_pos + self.instructions[self.i + 1] ]
                    except : number_one = 0
                elif mode_one == 1 :
                    try : number_one = self.instructions[self.i + 1]
                    except : number_one = 0                
                else :
                    try : number_one = self.instructions[ self.instructions[self.i + 1] ]
                    except : number_one = 0                  
    
                if operation % 100 != 9 :
                    if mode_two == 2 :
                        try : number_two = self.instructions[ self.relative_pos + self.instructions[self.i + 2] ]
                        except : number_two = 0
                    elif mode_two == 1 :
                        try : number_two = self.instructions[self.i + 2]
                        except : number_two = 0                    
                    else :
                        try : number_two = self.instructions[ self.instructions[self.i + 2] ]
                        except : number_two = 0
    
                if operation % 100 == 1 or operation % 100 == 2 or operation % 100 == 7 or operation % 100 == 8 :
                    if mode_three == 2 :
                        write_index = self.relative_pos + self.instructions[self.i + 3]
                    else :
                        write_index = self.instructions[self.i + 3]
    
            if operation % 100 == 1:
                self.instructions[write_index] = number_one + number_two
                self.i += 4
            elif operation % 100 == 2:     
                self.instructions[write_index] = number_one * number_two
                self.i += 4
            elif operation % 100 == 3:
                try : input_colour = self.painted_tiles[( self.x, self.y )]
                except : input_colour = 0
                if mode_one == 2 :
                    self.instructions[ self.relative_pos + self.instructions[self.i + 1] ] = int( input_colour )
                else :
                    self.instructions[ self.instructions[self.i + 1] ] = int( input_colour )
                self.i += 2
            elif operation % 100 == 4:
                if mode_one == 2 :
                    try : print_number = self.instructions[ self.relative_pos + self.instructions[self.i + 1] ]
                    except: print_number = 0
                elif mode_one == 1 :
                    print_number = self.instructions[self.i + 1] if self.i + 1 < len( self.instructions ) else 0
                    try : print_number = self.instructions[self.i + 1]
                    except : print_number = 0
                else :
                    try : print_number = self.instructions[ self.instructions[self.i + 1] ]
                    except : print_number = 0                
                self.i += 2
                self.output.append( print_number )
                if len( self.output ) == 2 :
                    # paint current tile
                    self.painted_tiles[( self.x, self.y )] = self.output[0]
                    
                    # rotate the robot
                    if self.output[1] == 1 :
                        self.direction = self.direction + 1 if self.direction < 3 else 0
                    else :
                        self.direction = self.direction - 1 if self.direction > 0 else 3
                    
                    # move the robot forward one
                    if self.direction == 0 : self.y -= 1
                    elif self.direction == 1 : self.x += 1
                    elif self.direction == 2 : self.y += 1
                    else : self.x -= 1
                    
                    self.output = []
            elif operation % 100 == 5:
                self.i = number_two if number_one else self.i + 3
            elif operation % 100 == 6:
                self.i = number_two if not number_one else self.i + 3
            elif operation % 100 == 7:
                self.instructions[write_index] = 1 if number_one < number_two else 0
                self.i += 4
            elif operation % 100 == 8:
                self.instructions[write_index] = 1 if number_one == number_two else 0
                self.i += 4
            elif operation % 100 == 9:
                self.relative_pos += number_one
                self.i += 2
                
    def print_drawing( self ) :
        min_x = None
        max_x = None
        min_y = None
        max_y = None
        
        for tile in self.painted_tiles :
            if min_x == None or tile[0] < min_x :
                min_x = tile[0]
            if max_x == None or tile[0] > max_x :
                max_x = tile[0]
            if min_y == None or tile[1] < min_y :
                min_y = tile[1]
            if max_y == None or tile[1] > max_y :
                max_y = tile[1]
        
        for i in range( min_y, max_y + 1 ) :
            for j in range( min_x, max_x + 1) :
                try :
                    tile = self.painted_tiles[( j, i )]
                except :
                    tile = 0
                if tile :
                    print( '#', end = '' )
                else :
                    print( '.', end = '' )
            print ( '' )

# Reads the file input.txt to get the input instruction, store the instruction as an array of ints
with open( "input.txt", "r" ) as fd:
    input_line = fd.readline().strip()
input_array = input_line.split( ',' )
input_array = [int( i ) for i in input_array]
input_dict = dict()

for i in range( 0, len( input_array ) ) :
    input_dict[i] = input_array[i]

painting_robot = Robot( input_dict )
painting_robot.run_diagnostic()
painting_robot.print_drawing()