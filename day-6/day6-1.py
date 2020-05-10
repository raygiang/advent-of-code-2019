def generate_orbit_dict( orbit_list ) :
    orbit_dict = dict()
    
    for orbit in orbit_list:
        orbit = orbit.split( ')' )
        orbit_dict[ orbit[1] ] = orbit[0]
        
    return orbit_dict

def count_orbits( orbit_dict ) :
    orbit_count = 0
    
    for orbit in orbit_dict :
        current_object = orbit
        while current_object != 'COM' :
            orbit_count += 1
            current_object = orbit_dict[current_object]
    
    return orbit_count        

orbit_list = []

# Reads the file input.txt to populate the orbit list
with open( "input.txt", "r" ) as fd:
    for line in fd:
        orbit_list.append( line.strip() )

orbit_dict = generate_orbit_dict( orbit_list )
print( count_orbits( orbit_dict ) )