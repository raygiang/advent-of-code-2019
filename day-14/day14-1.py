import re
import math

def find_ore_needed( recipe_dict, ingredient, qty_needed, leftover_mats ) :
    if qty_needed == 0 : return 0

    if ingredient == 'ORE' :
        return qty_needed
    else :
        requirements = recipe_dict[ ingredient ][:]
        amount_created = requirements.pop( 0 )
        ore_total = 0
        
        for requirement in requirements :
            try : amount_existing = leftover_mats[ingredient]
            except : amount_existing = 0
            if qty_needed - amount_existing > 0 :
                qty_needed -= amount_existing
                leftover_mats[ingredient] = 0
            elif amount_existing - qty_needed >= 0 :
                leftover_mats[ingredient] -= qty_needed
                qty_needed = 0

            amount_to_create = math.ceil( qty_needed / amount_created ) * requirement[1]
            ore_total += find_ore_needed( recipe_dict, requirement[0], amount_to_create, leftover_mats )
            
        leftover_qty = amount_created * math.ceil( qty_needed / amount_created ) - qty_needed
        
        if leftover_qty :
            try : leftover_mats[ingredient] += leftover_qty
            except : leftover_mats[ingredient] = leftover_qty
        
        return ore_total

recipe_list = []

# Reads the file input.txt to get the input instruction, store the instruction as an array of ints
with open( "input.txt", "r" ) as fd:
    for line in fd:
        recipe_list.append( line.strip() )

recipe_list = [ re.findall( r"[\d]+\s[\w]+", i ) for i in recipe_list ]
recipe_dict = {}
leftover_mats = {}

for recipe in recipe_list :
    result = recipe.pop().split()
    ingredients = []
    ingredients.append( int( result[0] ) )
    
    for ingredient in recipe :
        ingredient = ingredient.split()
        ingredients.append( ( ingredient[1], int( ingredient[0] ) ) )
    
    recipe_dict[result[1]] = ingredients

print( find_ore_needed( recipe_dict, 'FUEL', 1, leftover_mats ) )