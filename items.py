import db

def add_item(game_name, game_username, availability_start, availability_end, platform, region, other_info, user_id):
    sql = """INSERT INTO items (game_name, game_username, availability_start, availability_end, platform, region, other_info, user_id)
             VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [game_name, game_username, availability_start, availability_end, platform, region, other_info, user_id])