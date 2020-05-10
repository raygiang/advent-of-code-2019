import math

def get_asteroid_angles( asteroids, current_asteroid ) :
    asteroid_angles = dict()
    
    for asteroid in asteroids :
        if asteroid != current_asteroid :
            slope = math.atan2( ( asteroid[0] - current_asteroid[0] ), ( asteroid[1] - current_asteroid[1] ) )
            if slope <= math.pi :
                slope = slope + 2 * math.pi
            try :
                asteroid_angles[slope].append( asteroid )
            except :
                asteroid_angles[slope] = [ asteroid ]

    return asteroid_angles

def vaporize_asteroids( asteroid_list, current_asteroid ) :
    asteroid_angles = list( asteroid_list.keys() )
    asteroid_angles.sort( reverse = True )
    finished_vaporize = False
    vaporize_count = 0
    
    while not finished_vaporize :
        asteroid_angles_copy = asteroid_angles[:]
        for angle in asteroid_angles :
            vaporize_count += 1
                
            if len( asteroid_list[angle] ) > 1 :
                asteroids_in_path = asteroid_list[angle][:]
                closest_distance = -1
                for asteroid in asteroids_in_path :
                    asteroid_distance = abs( asteroid[1] - current_asteroid[1] ) + abs( asteroid[0] - current_asteroid[0] )
                    if closest_distance == -1 or asteroid_distance < closest_distance :
                        closest_distance = asteroid_distance
                        closest_asteroid = asteroid
                if vaporize_count == 200 :
                    print ( closest_asteroid )
                asteroid_list[angle].remove( closest_asteroid )
            else :
                if vaporize_count == 200 :
                    print ( asteroid_list[angle][0] )  
                asteroid_angles_copy.remove( angle )
                del asteroid_list[angle]
        if len( asteroid_angles_copy ) < 1 :
            finished_vaporize = True
        else :
            asteroid_angles = asteroid_angles_copy

# Reads the file input.txt to get the asteroid map
asteroid_map = []
asteroids = []

with open( "input.txt", "r" ) as fd:
    for line in fd:
        asteroid_map.append( line.strip() )

# Fill the asteroids array with the location of all asteroids
for i in range( len( asteroid_map ) ) :
    for j in range( len( asteroid_map[i] ) ) :
        if asteroid_map[i][j] == '#':
            asteroids.append( ( j, i ) )

current_asteroid = ( 28, 29 )

asteroid_list = get_asteroid_angles( asteroids, current_asteroid )

vaporize_asteroids( asteroid_list, current_asteroid )
