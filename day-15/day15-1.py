import math

# Returns the diagnostic code by running the algorithm on instruction list
def run_program( instruction_list, traversed_spots, moved_x = 0, moved_y = 0, initial_index = 0, init_rel_pos = 0 ) :
    i = initial_index
    relative_pos = init_rel_pos
    
    current_spot = ( moved_x, moved_y )
    try : 
        return not traversed_spots[ current_spot ]
    except :
        traversed_spots[ current_spot ] = True
    
    while i < len( instruction_list ) :
        operation = instruction_list[i]

        if operation == 99:
            return False

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
            best_solution = None
            best_move = None
            
            for j in range( 1, 5 ) :
                instruction_list_copy = instruction_list[:]
                
                if mode_one == 2 :
                    instruction_list_copy[ relative_pos + instruction_list_copy[i + 1] ] = j
                else :
                    instruction_list_copy[ instruction_list_copy[i + 1] ] = j
                i = i + 2
                
                if j == 1 :
                    solution = run_program( instruction_list_copy, traversed_spots, moved_x, moved_y - 1, i, relative_pos )
                elif j == 2 :
                    solution = run_program( instruction_list_copy, traversed_spots, moved_x, moved_y + 1, i, relative_pos )
                elif j == 3 :
                    solution = run_program( instruction_list_copy, traversed_spots, moved_x - 1, moved_y, i, relative_pos )
                elif j == 4 :
                    solution = run_program( instruction_list_copy, traversed_spots, moved_x + 1, moved_y, i, relative_pos )
                    
                if solution :
                    if best_solution == None or len( solution ) < len( best_solution ) :
                        best_solution = solution
                        best_move = j
                elif solution == 0 :
                    return False
            
            if best_solution :
                best_solution.insert( 0, best_move )
                return best_solution
            else :
                return False
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

            if print_number == 2 : return []
            i = i + 2
        elif operation % 100 == 5:
            i = number_two if number_one else i + 3
        elif operation % 100 == 6:
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

input_array = input_line.split( ',' )
input_array = [int( i ) for i in input_array]

traversed_spots = {}

print( run_program( input_array, traversed_spots ) )
