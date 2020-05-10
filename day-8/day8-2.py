# decode an image in the form of multiple layers
def decode_image( layers ) :
    decoded_image = dict()
    remaining_pixels = list( range( 150 ) )
    
    for layer in layers :
        new_remaining_pixels = remaining_pixels[:]
        for pixel in remaining_pixels :
            if layer[pixel] == '1' or layer[pixel] == '0' :
                decoded_image[pixel] = layer[pixel]
                new_remaining_pixels.remove( pixel )
        remaining_pixels = new_remaining_pixels[:]
    
    for i in range( 150 ) :
        if not i in decoded_image:
            print ( ' ', end = '' )
        else:
            print ( decoded_image[i], end = '' )
        if ( i + 1 ) % 25 == 0 :
            print ( '' )

# Reads the file input.txt to get the encoded picture
with open( "input.txt", "r" ) as fd:
    input_line = fd.readline().strip()
layers = [ input_line[i : i + 150] for i in range( 0, len( input_line ), 150 ) ]

decode_image( layers )
