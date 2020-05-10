import re
import itertools

class Moon:
    def __init__( self, initial_position ) :
        self.x = int( initial_position[0] )
        self.y = int( initial_position[1] )
        self.z = int( initial_position[2] )
        self.x_vel = 0
        self.y_vel = 0
        self.z_vel = 0
        
    def update_velocity( self, other_moon ) :
        if other_moon.x > self.x :
            self.x_vel += 1
        elif other_moon.x < self.x :
            self.x_vel -= 1
            
        if other_moon.y > self.y :
            self.y_vel += 1
        elif other_moon.y < self.y :
            self.y_vel -= 1
            
        if other_moon.z > self.z :
            self.z_vel += 1
        elif other_moon.z < self.z :
            self.z_vel -= 1
        
    def move_moon( self ) :
        self.x += self.x_vel
        self.y += self.y_vel
        self.z += self.z_vel
        
    def get_total_energy( self ) :
        pot_energy = abs( self.x ) + abs( self.y ) + abs( self.z )
        kin_energy = abs( self.x_vel ) + abs( self.y_vel ) + abs( self.z_vel )
        
        return pot_energy * kin_energy

initial_moon_positions = []

# Reads the file input.txt to get the input instruction, store the instruction as an array of ints
with open( "input.txt", "r" ) as fd:
    for line in fd:
        initial_moon_positions.append( line.strip()[1:-1] )

initial_moon_positions = [ re.findall( r"[-\d]+", i ) for i in initial_moon_positions ]
moons = [ Moon( position ) for position in initial_moon_positions ]
moon_pairs = list( itertools.combinations( moons, 2 ) )

for i in range( 1000 ) :
    for pair in moon_pairs :
        pair[0].update_velocity( pair[1] )
        pair[1].update_velocity( pair[0] )
    for moon in moons :
        moon.move_moon()
    
total_energy = 0
for moon in moons :
    print ( moon.get_total_energy(), moon.x, moon.y, moon.z, moon.x_vel, moon.y_vel, moon.z_vel )
    total_energy += moon.get_total_energy()
    
print ( total_energy )