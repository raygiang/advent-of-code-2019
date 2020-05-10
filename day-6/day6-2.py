def generate_orbit_dict( orbit_list ) :
    orbit_dict = dict()
    
    for orbit in orbit_list:
        orbit = orbit.split( ')' )
        orbit_dict[ orbit[1] ] = orbit[0]
        
    return orbit_dict

def get_path( orbit_dict, obj ) :
    path_dict = dict()
    distance = 0
    obj = orbit_dict[obj]
    
    while obj != 'COM' :
        distance += 1
        obj = orbit_dict[obj]
        path_dict[obj] = distance
    
    return path_dict

orbit_list = []

# Reads the file input.txt to populate the orbit list
with open( "input.txt", "r" ) as fd:
    for line in fd:
        orbit_list.append( line.strip() )

orbit_dict = generate_orbit_dict( orbit_list )

you_path = get_path( orbit_dict, 'YOU' )
santa_path = get_path( orbit_dict, 'SAN' )

intersections = ( set( you_path ).intersection( santa_path ) )

min_transfers = 0

for intersection in intersections:
    transfers = you_path[intersection] + santa_path[intersection]
    if min_transfers == 0 or transfers < min_transfers :
        min_transfers = transfers
        
print ( min_transfers )