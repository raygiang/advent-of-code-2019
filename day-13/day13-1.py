import math
from itertools import permutations

class ArcadeGame:
    def __init__( self, instruction_list ) :
        self.instructions = instruction_list
        self.i = 0
        self.relative_pos = 0
        self.output = []
        self.game_tiles = dict()
        self.game_instructions = []
        
    def run_program( self ) :
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
                self.output.append( print_number )
                self.i += 2
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

        for i in range( 0, len( self.output ), 3 ) :
            self.game_instructions.append( ( self.output[i], self.output[i + 1], self.output[i + 2] ) )
    
    def play_game( self ) :
        for instruction in self.game_instructions :
            self.game_tiles[( instruction[0], instruction[1] )] = instruction[2]

# Reads the file input.txt to get the input instruction, store the instruction as an array of ints
with open( "input.txt", "r" ) as fd:
    input_line = fd.readline().strip()
input_array = input_line.split( ',' )
input_array = [int( i ) for i in input_array]
input_dict = dict()

for i in range( 0, len( input_array ) ) :
    input_dict[i] = input_array[i]

arcade_game = ArcadeGame( input_dict )
arcade_game.run_program()
arcade_game.play_game()

block_tiles = 0

for tile in arcade_game.game_tiles :
    if arcade_game.game_tiles[tile] == 2 :
        block_tiles += 1
        
print ( block_tiles )