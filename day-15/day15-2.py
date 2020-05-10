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
        self.current_instruction = []
        self.paddle_position = None
        self.ball_position = None
        
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
                self.display_game()
                distance_difference = self.ball_position[0] - self.paddle_position[0]
                if distance_difference > 0 : joystick_input = 1
                elif distance_difference < 0 : joystick_input = -1
                else: joystick_input = 0
                if mode_one == 2 :
                    self.instructions[ self.relative_pos + self.instructions[self.i + 1] ] = joystick_input
                else :
                    self.instructions[ self.instructions[self.i + 1] ] = joystick_input
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
                self.current_instruction.append( print_number )
                if len( self.current_instruction ) == 3 :
                    self.game_instructions.append( ( self.current_instruction[0], self.current_instruction[1], self.current_instruction[2] ) )
                    if self.current_instruction[2] == 3 :
                        self.paddle_position = ( self.current_instruction[0], self.current_instruction[1] )
                    if self.current_instruction[2] == 4 :
                        self.ball_position = ( self.current_instruction[0], self.current_instruction[1] )
                    self.current_instruction = []
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
    
    def display_game( self ) :
        min_x = None
        max_x = None
        min_y = None
        max_y = None
        
        for instruction in self.game_instructions :
            if min_x == None or instruction[0] < min_x :
                min_x = instruction[0]
            if max_x == None or instruction[0] > max_x :
                max_x = instruction[0]
            if min_y == None or instruction[1] < min_y :
                min_y = instruction[1]
            if max_y == None or instruction[1] > max_y :
                max_y = instruction[1]
                
            self.game_tiles[( instruction[0], instruction[1] )] = instruction[2] 
        
        if len( self.game_tiles ) :
            for i in range( min_y, max_y + 1 ) :
                for j in range( 0, max_x + 1) :
                    try :
                        tile = self.game_tiles[( j, i )]
                    except :
                        tile = 0
                    if tile == 2 :
                        print( '#', end = '' )
                    elif tile == 4 :
                        print( 'O', end = '' )
                    elif tile == 3 :
                        print( '_', end = '' )                            
                    elif tile :
                        print( tile, end = '' )
                    else :
                        print( ' ', end = '' )
                print ( '' )   

# Reads the file input.txt to get the input instruction, store the instruction as an array of ints
with open( "input.txt", "r" ) as fd:
    input_line = fd.readline().strip()
input_array = input_line.split( ',' )
input_array = [int( i ) for i in input_array]
input_array[0] = 2 # Play for free as per instructions
input_dict = dict()

for i in range( 0, len( input_array ) ) :
    input_dict[i] = input_array[i]

arcade_game = ArcadeGame( input_dict )
arcade_game.run_program()
arcade_game.display_game()

print ( arcade_game.game_tiles[( -1, 0 )] )