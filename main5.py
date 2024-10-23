def get_quest_status(progress):
    try:
       return progress['quests']['Dragon Slayer']['status']
    except KeyError:
        return None