import math

with open( "input.txt", "r" ) as fd:
    input_line = fd.readline().strip()

input_array = input_line.split( ',' )
input_array = [int( i ) for i in input_array]
input_array[1] = 12
input_array[2] = 2

for i in range( 0, len( input_array ), 4 ) :
    operation = input_array[i]
    if operation == 99:
        break    
    
    index_1 = input_array[i + 1]
    index_2 = input_array[i + 2]
    index_3 = input_array[i + 3]

    if operation == 1:
        input_array[index_3] = input_array[index_1] + input_array[index_2]
    elif operation == 2:
        input_array[index_3] = input_array[index_1] * input_array[index_2]
    
print ( input_array )