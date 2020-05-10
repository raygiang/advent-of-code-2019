import math

# Returns the diagnostic code by running the algorithm on instruction list
def run_diagnostic( instruction_list ) :
    i = 0
    while i < len( instruction_list ) :
        operation = instruction_list[i]
        if operation == 99:
            break
        
        mode_one = math.floor( operation % 1000 / 100 )
        mode_two = math.floor( operation % 10000 / 1000 )
        
        if not operation % 100 == 3 and not operation % 100 == 4 :
            number_one = instruction_list[i + 1] if mode_one else instruction_list[ instruction_list[i + 1] ]
            number_two = instruction_list[i + 2] if mode_two else instruction_list[ instruction_list[i + 2] ]            

        if operation % 100 == 1:
            write_index = instruction_list[i + 3]            
            instruction_list[write_index] = number_one + number_two
            i = i + 4
        elif operation % 100 == 2:
            write_index = instruction_list[i + 3]            
            instruction_list[write_index] = number_one * number_two
            i = i + 4
        elif operation % 100 == 3:
            input_text = input("Enter your command: ")
            instruction_list[ instruction_list[i + 1] ] = int( input_text )
            i = i + 2
        elif operation % 100 == 4:
            print_number = instruction_list[i + 1] if mode_one else instruction_list[ instruction_list[i + 1] ]
            print ( print_number )
            i = i + 2
        elif operation % 100 == 5:
            i = number_two if number_one else i + 3
        elif operation % 100 == 6:
            i = number_two if not number_one else i + 3
        elif operation % 100 == 7:
            write_index = instruction_list[i + 3]
            instruction_list[write_index] = 1 if number_one < number_two else 0
            i = i + 4
        elif operation % 100 == 8:
            write_index = instruction_list[i + 3]
            instruction_list[write_index] = 1 if number_one == number_two else 0
            i = i + 4

# Reads the file input.txt to get the input instruction, store the instruction as an array of ints
with open( "input.txt", "r" ) as fd:
    input_line = fd.readline().strip()
input_array = input_line.split( ',' )
input_array = [int( i ) for i in input_array]

run_diagnostic( input_array )
