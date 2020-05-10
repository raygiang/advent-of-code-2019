import math

# Returns the output by running the algorithm on instruction list with the given noun and verb
def find_output( instruction_list, noun, verb ) :
    instruction_copy = instruction_list[:]
    instruction_copy[1] = noun
    instruction_copy[2] = verb
    
    for i in range( 0, len( instruction_copy ), 4 ) :
        operation = instruction_copy[i]
        if operation == 99:
            break
        
        index_1 = instruction_copy[i + 1]
        index_2 = instruction_copy[i + 2]
        index_3 = instruction_copy[i + 3]
        
        if operation == 1:
            instruction_copy[index_3] = instruction_copy[index_1] + instruction_copy[index_2]
        elif operation == 2:
            instruction_copy[index_3] = instruction_copy[index_1] * instruction_copy[index_2]
            
    return instruction_copy[0]

# Reads the file input.txt to get the input instruction, store the instruction as an array of ints
with open( "input.txt", "r" ) as fd:
    input_line = fd.readline().strip()
input_array = input_line.split( ',' )
input_array = [int( i ) for i in input_array]

for noun in range( 0, 100 ) :
    for verb in range( 0, 100 ) :
        if find_output( input_array, noun, verb ) == 19690720 :
            print ( 100 * noun + verb )
            print ( noun, verb )
        
