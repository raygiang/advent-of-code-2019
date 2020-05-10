import math
from itertools import permutations

class Amplifier:
    
    def __init__( self, instruction_list, phase_setting ) :
        self.instructions = instruction_list
        self.i = 0
        self.phase_setting = phase_setting
        self.initial_run = True
        
    def run_diagnostic( self, signal ) :
        while self.i < len( self.instructions ) :
            operation = self.instructions[self.i]
            if operation == 99:
                break
    
            mode_one = math.floor( operation % 1000 / 100 )
            mode_two = math.floor( operation % 10000 / 1000 )
    
            if not operation % 100 == 3 and not operation % 100 == 4 :
                number_one = self.instructions[self.i + 1] if mode_one else self.instructions[ self.instructions[self.i + 1] ]
                number_two = self.instructions[self.i + 2] if mode_two else self.instructions[ self.instructions[self.i + 2] ]            
    
            if operation % 100 == 1:
                write_index = self.instructions[self.i + 3]            
                self.instructions[write_index] = number_one + number_two
                self.i = self.i + 4
            elif operation % 100 == 2:
                write_index = self.instructions[self.i + 3]            
                self.instructions[write_index] = number_one * number_two
                self.i = self.i + 4
            elif operation % 100 == 3:
                input_value = self.phase_setting if self.initial_run else signal
                self.initial_run = False
                self.instructions[ self.instructions[self.i + 1] ] = input_value
                self.i = self.i + 2
            elif operation % 100 == 4:
                return_signal = self.instructions[self.i + 1] if mode_one else self.instructions[ self.instructions[self.i + 1] ]
                self.i = self.i + 2
                return ( return_signal )
            elif operation % 100 == 5:
                self.i = number_two if number_one else self.i + 3
            elif operation % 100 == 6:
                self.i = number_two if not number_one else self.i + 3
            elif operation % 100 == 7:
                write_index = self.instructions[self.i + 3]
                self.instructions[write_index] = 1 if number_one < number_two else 0
                self.i = self.i + 4
            elif operation % 100 == 8:
                write_index = self.instructions[self.i + 3]
                self.instructions[write_index] = 1 if number_one == number_two else 0
                self.i = self.i + 4

# Reads the file input.txt to get the input instruction, store the instruction as an array of ints
with open( "input.txt", "r" ) as fd:
    input_line = fd.readline().strip()
input_array = input_line.split( ',' )
input_array = [int( i ) for i in input_array]

permutation_list = set ( permutations( [5, 6, 7, 8, 9] ) )
highest_signal = 0

for permutation in permutation_list :
    amplifiers = []
    current_signal = 0
    
    # Create the five amplifiers with a phase setting and their own copy of instructions
    for i in permutation :
        amplifiers.append( Amplifier( input_array[:], i ) )
        
    while True :
        for amp in amplifiers :
            new_signal = amp.run_diagnostic( current_signal )
            if new_signal :
                current_signal = new_signal
            else :
                break
        if not new_signal :
            break
    highest_signal = current_signal if current_signal > highest_signal else highest_signal
    
print ( highest_signal )
