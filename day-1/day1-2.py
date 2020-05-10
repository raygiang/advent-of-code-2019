import math

sum = 0

with open( "input.txt", "r" ) as fd:
    for line in fd:
        line = line.strip()
        mass = float( line )
        current_total = 0
        
        while True:
            fuel = math.floor( mass / 3 ) - 2
            if fuel <= 0 :
                break
            current_total += fuel
            mass = fuel
            
        sum += current_total
        
print ( sum )