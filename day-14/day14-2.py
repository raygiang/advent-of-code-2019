import re
import math

def find_ore_needed( recipe_dict, ingredient, qty_needed, leftover_mats ) :
    if qty_needed == 0 : return 0
    
    try : amount_existing = leftover_mats[ingredient]
    except : amount_existing = 0
    if qty_needed - amount_existing > 0 :
        qty_needed -= amount_existing
        leftover_mats[ingredient] = 0
    elif amount_existing - qty_needed >= 0 :
        leftover_mats[ingredient] -= qty_needed
        qty_needed = 0
        
    if ingredient == 'ORE' :
        return qty_needed
    else :
        requirements = recipe_dict[ ingredient ][:]
        amount_created = requirements.pop( 0 )
        ore_total = 0
        
        for requirement in requirements :
            amount_to_create = math.ceil( qty_needed / amount_created ) * requirement[1]
            ore_total += find_ore_needed( recipe_dict, requirement[0], amount_to_create, leftover_mats )
            
        leftover_qty = amount_created * math.ceil( qty_needed / amount_created ) - qty_needed
        
        if leftover_qty :
            try : leftover_mats[ingredient] += leftover_qty
            except : leftover_mats[ingredient] = leftover_qty
        
        return ore_total
    
def find_produceable_fuel( recipe_dict, lower_bound, upper_bound ) :
    while True :
        leftover_mats = {}
        leftover_mats['ORE'] = 1000000000000
        
        mid_distance = math.floor( ( upper_bound - lower_bound ) / 2 )
        if not mid_distance : break
        fuel_count = lower_bound + mid_distance
        
        ore_needed = find_ore_needed( recipe_dict, 'FUEL', fuel_count, leftover_mats )
        
        if not ore_needed :
            lower_bound = fuel_count
        else :
            upper_bound = fuel_count
        
    print( fuel_count )

recipe_list = []

# Reads the file input.txt to get the input instruction, store the instruction as an array of ints
with open( "input.txt", "r" ) as fd:
    for line in fd:
        recipe_list.append( line.strip() )

recipe_list = [ re.findall( r"[\d]+\s[\w]+", i ) for i in recipe_list ]
recipe_dict = {}

for recipe in recipe_list :
    result = recipe.pop().split()
    ingredients = []
    ingredients.append( int( result[0] ) )
    
    for ingredient in recipe :
        ingredient = ingredient.split()
        ingredients.append( ( ingredient[1], int( ingredient[0] ) ) )
    
    recipe_dict[result[1]] = ingredients
    
ore_for_one_fuel = ore_needed = find_ore_needed( recipe_dict, 'FUEL', 1, {} )
lower_bound = int( 1000000000000 / ore_for_one_fuel )
upper_bound = int( math.pow( ore_for_one_fuel, 2 ) )

find_produceable_fuel( recipe_dict, lower_bound, upper_bound )

