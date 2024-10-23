def get_most_common_enemy(enemies_dict):
    if not enemies_dict:
        return None
    
    
    most_common_enemy= None
    highest_count=0
    for enemy ,count in enemies_dict.items():
        if count> highest_count:
            most_common_enemy =enemy
            highest_count =count 
    return most_common_enemy

    
  
