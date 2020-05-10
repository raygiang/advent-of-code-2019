import math

def visible_asteroids( asteroids, current_asteroid ) :
    visible_asteroids = dict()
    
    for asteroid in asteroids :
        if asteroid != current_asteroid :
            slope = math.atan2( ( asteroid[0] - current_asteroid[0] ), ( asteroid[1] - current_asteroid[1] ) )
            visible_asteroids[slope] = True
            
    return len( visible_asteroids )

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
            
max_num_asteroids = -1

for asteroid in asteroids :
    current_max = visible_asteroids( asteroids, asteroid )
    if max_num_asteroids == -1 or current_max > max_num_asteroids :
        max_num_asteroids = current_max
        ideal_asteroid = asteroid
    
print( max_num_asteroids, ideal_asteroid )
