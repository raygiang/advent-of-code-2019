# Return the plot of the line relative to the origin, keeping in mind the number of steps taken to reach each point
def find_line_plot( line ) :
    line_points = dict()
    current_x = 0
    current_y = 0
    current_steps = 0
    
    for instruction in line :
        direction = instruction[0]
        amount = int( instruction[1:] )
        
        for i in range( 0, amount ) :
            if direction == 'U':
                current_y += 1
            elif direction == 'D' :
                current_y -= 1
            elif direction == 'R' :
                current_x += 1
            elif direction == 'L' :
                current_x -= 1
            line_points[ (current_x, current_y) ] = current_steps + i + 1;
        
        current_steps += amount
    
    return line_points

# Reads the file input.txt to get the input lines
with open( "input.txt", "r" ) as fd:
    input_line = fd.readline().strip()
    line_one = input_line.split( ',' )
    input_line = fd.readline().strip()
    line_two = input_line.split( ',' )
    
# Get the plot for the two lines and find the intersections
line_one_plot = find_line_plot( line_one )
line_two_plot = find_line_plot( line_two )
intersections = set( line_one_plot ).intersection( line_two_plot )

closest_distance = 0

# Find the intersection with the closest steps to the origin
for intersection in intersections:
    distance = line_one_plot[intersection] + line_two_plot[intersection]
    if closest_distance == 0 or distance < closest_distance :
        closest_distance = distance

print ( closest_distance )