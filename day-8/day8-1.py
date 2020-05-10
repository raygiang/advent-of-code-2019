# Reads the file input.txt to get the encoded picture
with open( "input.txt", "r" ) as fd:
    input_line = fd.readline().strip()
layers = [ input_line[i : i + 150] for i in range( 0, len( input_line ), 150 ) ]

lowest_zeros = -1

# Find the layer with the smallest number of 0 and keep track of the number of 1 and 2
for layer in layers :
    num_zeros = layer.count( '0' )
    if lowest_zeros == -1 or num_zeros < lowest_zeros :
        lowest_zeros = num_zeros
        num_ones = layer.count( '1' )
        num_twos = layer.count( '2' )
    
print ( num_ones * num_twos )
    