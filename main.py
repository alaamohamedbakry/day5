def get_character_record(name, server, level, rank):
    charcter_id=f"{name}#{server}"
    return{
        "name":name,
        "server":server,
        "level":level,
        "rank":rank,
        "id":charcter_id
    }
