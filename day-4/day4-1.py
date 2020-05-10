# The range given
lower_limit = 193651
upper_limit = 649729

valid_counter = 0

# Check all numbers within the range to see if they are valid
for num in range( lower_limit, upper_limit ) :
    adjacent_flag = False
    decreasing_flag = False
    prev_num = None
    num = str( num )
    
    for i in num:
        curr_num = int( i )
        if prev_num :
            if not adjacent_flag and prev_num == curr_num :
                adjacent_flag = True
            if not decreasing_flag and curr_num < prev_num :
                decreasing_flag = True
                break
            
        prev_num = curr_num
    
    if adjacent_flag and not decreasing_flag :
        valid_counter += 1
        
print ( valid_counter )
