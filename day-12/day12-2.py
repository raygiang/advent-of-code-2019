import re
import itertools
import math

class Moon:
    def __init__( self, initial_position ) :
        self.init_x = int( initial_position[0] )
        self.x = self.init_x
        self.init_y = int( initial_position[1] )
        self.y = self.init_y
        self.init_z = int( initial_position[2] )
        self.z = self.init_z
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
    
def find_lcm( nums ) :
    lcm = nums[0]
    
    for num in nums[1:] :
        lcm = lcm * int( num / math.gcd( lcm, num ) )
        
    return lcm

initial_moon_positions = []

# Reads the file input.txt to get the input instruction, store the instruction as an array of ints
with open( "input.txt", "r" ) as fd:
    for line in fd:
        initial_moon_positions.append( line.strip()[1:-1] )

initial_moon_positions = [ re.findall( r"[-\d]+", i ) for i in initial_moon_positions ]
moons = [ Moon( position ) for position in initial_moon_positions ]
moon_pairs = list( itertools.combinations( moons, 2 ) )

positions_occured = dict()
steps_taken = 0
x_steps = 0
y_steps = 0
z_steps = 0

while True :
    steps_taken += 1
    
    for pair in moon_pairs :
        pair[0].update_velocity( pair[1] )
        pair[1].update_velocity( pair[0] )
        
    position = []
    
    for moon in moons :
        moon.move_moon()
        position.append( moon.x == moon.init_x and moon.x_vel == 0 )
        position.append( moon.y == moon.init_y and moon.y_vel == 0 )
        position.append( moon.z == moon.init_z and moon.z_vel == 0 )
        
    if not x_steps :
        if position[0] == position[3] == position[6] == position[9] == True :
            x_steps = steps_taken
    if not y_steps :
        if position[1] == position[4] == position[7] == position[10] == True :
            y_steps = steps_taken
    if not z_steps :
        if position[2] == position[5] == position[8] == position[11] == True :
            z_steps = steps_taken
        
    if x_steps and y_steps and z_steps :
        break

print ( find_lcm( [ x_steps, y_steps, z_steps ] ) )