import db

def add_item(game_name, game_username, availability_time, platform, region, other_info, user_id):
    sql = """INSERT INTO items (game_name, game_username, availability_time, platform, region, other_info, user_id)
             VALUES (?, ?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [game_name, game_username, availability_time, platform, region, other_info, user_id])

def get_items():
    sql = "SELECT id, game_name FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.game_name,
                    items.game_username,
                    items.availability_time,
                    items.platform,
                    items.region,
                    items.other_info
             FROM items, users
             WHERE items.user_id = users.id
             AND items.id = ?"""
    return db.query(sql, [item_id])[0]