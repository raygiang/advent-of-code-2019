# Return the plot of the line relative to the origin
def find_line_plot( line ) :
    line_points = []
    current_x = 0
    current_y = 0
    
    for instruction in line :
        direction = instruction[0]
        amount = int( instruction[1:] )
        
        for i in range( 0, amount ) :
            if direction == 'U':
                current_y += 1
                line_points.append( (current_x, current_y) )
            elif direction == 'D' :
                current_y -= 1
                line_points.append( (current_x, current_y) )
            elif direction == 'R' :
                current_x += 1
                line_points.append( (current_x, current_y) )
            elif direction == 'L' :
                current_x -= 1
                line_points.append( (current_x, current_y) )
    
    return set( line_points )

# Reads the file input.txt to get the input lines
with open( "input.txt", "r" ) as fd:
    input_line = fd.readline().strip()
    line_one = input_line.split( ',' )
    input_line = fd.readline().strip()
    line_two = input_line.split( ',' )
    
# Get the plot for the two lines and find the intersections
line_one_plot = find_line_plot( line_one )
line_two_plot = find_line_plot( line_two )
intersections = line_one_plot.intersection( line_two_plot )

closest_distance = 0

# Find the intersection with the closest distance to the origin
for intersection in intersections:
    distance = abs( intersection[0] ) + abs( intersection[1] )
    if closest_distance == 0 or distance < closest_distance :
        closest_distance = distance

print ( closest_distance )