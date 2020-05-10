import math

# Returns the diagnostic code by running the algorithm on instruction list
def run_diagnostic( instruction_list ) :
    i = 0
    relative_pos = 0
    
    while i < len( instruction_list ) :
        operation = instruction_list[i]

        if operation == 99:
            break

        mode_one = math.floor( operation % 1000 / 100 )
        mode_two = math.floor( operation % 10000 / 1000 )
        mode_three = math.floor( operation % 100000 / 10000 )
        
        if operation % 100 != 3 and operation % 100 != 4 :
            if mode_one == 2 :
                try : number_one = instruction_list[ relative_pos + instruction_list[i + 1] ]
                except : number_one = 0
            elif mode_one == 1 :
                try : number_one = instruction_list[i + 1]
                except : number_one = 0                
            else :
                try : number_one = instruction_list[ instruction_list[i + 1] ]
                except : number_one = 0                  

            if operation % 100 != 9 :
                if mode_two == 2 :
                    try : number_two = instruction_list[ relative_pos + instruction_list[i + 2] ]
                    except : number_two = 0
                elif mode_two == 1 :
                    try : number_two = instruction_list[i + 2]
                    except : number_two = 0                    
                else :
                    try : number_two = instruction_list[ instruction_list[i + 2] ]
                    except : number_two = 0

            if operation % 100 == 1 or operation % 100 == 2 or operation % 100 == 7 or operation % 100 == 8 :
                if mode_three == 2 :
                    write_index = relative_pos + instruction_list[i + 3]
                else :
                    write_index = instruction_list[i + 3]

        if operation % 100 == 1:
            instruction_list[write_index] = number_one + number_two
            i = i + 4
        elif operation % 100 == 2:     
            instruction_list[write_index] = number_one * number_two
            i = i + 4
        elif operation % 100 == 3:
            input_text = input("Enter your command: ")
            if mode_one == 2 :
                instruction_list[ relative_pos + instruction_list[i + 1] ] = int( input_text )
            else :
                instruction_list[ instruction_list[i + 1] ] = int( input_text )
            i = i + 2
        elif operation % 100 == 4:
            if mode_one == 2 :
                try : print_number = instruction_list[ relative_pos + instruction_list[i + 1] ]
                except: print_number = 0
            elif mode_one == 1 :
                print_number = instruction_list[i + 1] if i + 1 < len( instruction_list ) else 0
                try : print_number = instruction_list[i + 1]
                except : print_number = 0
            else :
                try : print_number = instruction_list[ instruction_list[i + 1] ]
                except : print_number = 0                
            print ( print_number )
            i = i + 2
        elif operation % 100 == 5:
            i = number_two if number_one else i + 3
        elif operation % 100 == 6:
            #print( 'wtf', not number_one, number_one )
            i = number_two if not number_one else i + 3
        elif operation % 100 == 7:
            instruction_list[write_index] = 1 if number_one < number_two else 0
            i = i + 4
        elif operation % 100 == 8:
            instruction_list[write_index] = 1 if number_one == number_two else 0
            i = i + 4
        elif operation % 100 == 9:
            relative_pos += number_one
            i = i + 2

# Reads the file input.txt to get the input instruction, store the instruction as an array of ints
with open( "input.txt", "r" ) as fd:
    input_line = fd.readline().strip()
#input_line = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
input_array = input_line.split( ',' )
input_array = [int( i ) for i in input_array]
input_dict = dict()

for i in range( 0, len( input_array ) ) :
    input_dict[i] = input_array[i]

run_diagnostic( input_dict )
